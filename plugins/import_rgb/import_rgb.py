#!/usr/bin/env python

"""Import Hugo content, generating metadata and converting as necessary"""

from dataclasses import dataclass, field
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import arrow
import frontmatter
from nikola.plugin_categories import Command
from nikola.utils import copy_file, get_logger, makedirs, remove_file, slugify
from ruamel.yaml import YAML

log = get_logger(os.path.basename(__file__))
yaml = YAML()
ARCHIVED_CATEGORIES = ("blogspot", "coolnamehere")
HUGO_CONFIG_SETTING = "IMPORT_RGB_CONFIG"


@dataclass
class HugoContent:
    """Knows enough about a Hugo content file to help import itself into Nikola"""

    hugo_file: Path
    content_dir: Path
    cover_image: Optional[str] = None
    bundle_files: List[str] = field(default_factory=list)
    frontmatter: Dict[str, Any] = field(init=False)
    content: str = field(init=False)
    is_post: bool = field(init=False)
    is_draft: bool = field(init=False)

    @property
    def content_format(self):
        if "format" in self.frontmatter:
            return self.frontmatter["format"]

        log.debug("No explicit format for %s", self.hugo_file)
        return self.hugo_file.suffix.replace(".", "")

    def __post_init__(self):
        log.info("post_init: %s", self.hugo_file)
        post = frontmatter.load(self.hugo_file)
        self.frontmatter = post.metadata
        self.content = post.content
        # put this here or it'll confuse date handling later.
        # yaml_text = re.sub(r"^(date: \d{4}-\d{2}-\d{2})T", r"\1 ", yaml_text)
        date = self.frontmatter.get("date", None)
        self.is_draft = self.frontmatter.get("draft", False)

        if date or self.is_draft:
            self.is_post = True
        else:
            self.is_post = False

        if self.is_draft and not date:
            self.set_date(arrow.get().date())

        bundle_dir = self.hugo_file.parent

        for item in bundle_dir.iterdir():
            # Lazy check if this is a cover image
            if item.name.startswith("cover"):
                self.cover_image = item.name
                self.bundle_files.append(item)
                log.info(f"{bundle_dir} -> {item}")

    def add_tag(self, tag):
        if self.has_tag(tag):
            return

        if "tags" not in self.frontmatter:
            self.frontmatter["tags"] = []

        self.frontmatter["tags"].append(tag)

    def preferred_path(self):
        """My location in the nikola site"""
        title_path = self.nikola_stub_folder()
        base_path = f"index.{self.content_format}"

        return os.path.join(title_path, base_path)

    def prep_content(self) -> str:
        """Perform necessary transformations for import to content body."""
        teaser_text = (
            ".. TEASER_END" if self.content_format == "rst" else "<!-- TEASER_END -->"
        )
        content = re.sub(
            r"^<!--more-->$", teaser_text, self.content, count=1, flags=re.MULTILINE
        )

        return content

    def nikola_stub_folder(self):
        "Return the stub folder path for this content in Nikola"
        title_path = slugify(self.frontmatter["title"])

        if self.is_post:
            date = self.frontmatter["date"]
            date_path = self.get_date().strftime("%Y/%m")

            return os.path.join(date_path, title_path)

        return title_path

    def generate_metadata(self) -> Dict[str, Any]:
        """convert Hugo frontmatter to key/values better suited to Nikola"""
        metadata = self.frontmatter

        if "category" in metadata:
            category = metadata.pop("category").lower()
            self.add_tag(category)

        if str(self.hugo_file).find("/note/") > 0:
            metadata["category"] = "note"
            metadata["type"] = "micro"
        elif str(self.hugo_file).find("/bookmark/") > 0:
            metadata["category"] = "bookmark"
            metadata["type"] = "micro"
        elif (
            str(self.hugo_file).find("/art/") > 0
            or self.has_tag("drawing")
            or self.has_tag("craft")
        ):
            metadata["category"] = "craft"
            metadata["type"] = "micro"

        # set `previewimage` metadata
        if self.cover_image:
            image_path = os.path.join(
                "/images/", self.nikola_stub_folder(), self.cover_image
            )
            log.info(image_path)
            metadata["previewimage"] = image_path

        return metadata

    def get_date(self):
        return self.frontmatter["date"]

    def has_tag(self, tag) -> bool:
        if "tags" not in self.frontmatter:
            return False

        return tag in self.frontmatter["tags"]

    def set_date(self, date):
        self.frontmatter["date"] = date

    def import_content(self):
        """Import content and supplemental files"""

        output_root = "posts" if self.is_post else "pages"
        self.write_to(output_root)
        # TODO: write cover image to `images/{dirname(preferred_path)}`
        if self.bundle_files:
            image_folder = os.path.join("images/", self.nikola_stub_folder())
            makedirs(image_folder)

            for bundle_file in self.bundle_files:
                copy_file(bundle_file, image_folder)
                log.info(f"Copied {bundle_file}")

    def write_to(self, destination: str):
        """Create a new nikola post using my content and frontmatter."""
        output_file = Path(destination) / self.preferred_path()
        output_dir = output_file.parent

        if output_dir.is_dir():
            better_indexes = [
                child.name
                for child in output_dir.iterdir()
                if child.suffix in [".adoc", ".rst"]
            ]

            if better_indexes:
                log.warn("I see %s; Skipping %s for now", better_indexes, output_dir)
                return

            lesser_indexes = [
                child for child in output_dir.iterdir() if child.suffix in [".md"]
            ]

            for old_file in lesser_indexes:
                log.warn("Deleting old imported content %s", old_file)
                old_file.unlink()

        metadata = self.generate_metadata()
        content = self.prep_content()
        log.debug(f"Writing [{metadata['title']}] to [{output_file}]]")

        makedirs(output_dir)
        DELIMITER = "---\n"

        with open(output_file, "w") as f:
            f.write(DELIMITER)
            yaml.dump(metadata, f)
            f.write(DELIMITER)
            f.write(content)


@dataclass
class HugoSite:
    """Knows enough about a Hugo site to help import its content into Nikola"""

    config_file: Path
    safe_extensions: Tuple[str]

    def collect_content_files(self) -> List[HugoContent]:
        """Return a list of files in the Hugo site that are safe for import"""
        site_dir = self.config_file.parent
        content_dir = site_dir / "content"
        content_files = []
        extensions: Dict[str, int] = {}

        for root, dirs, files in os.walk(content_dir):
            root_path = Path(root)

            for filename in files:
                if filename.startswith("_"):
                    # leading underscores are for section summaries.
                    continue

                if filename.endswith("~"):
                    # A backup file got in there somehow.
                    continue

                full_path = root_path / filename
                ext = full_path.suffix
                extensions[ext] = extensions.get(ext, 0) + 1

                if ext not in self.safe_extensions:
                    log.debug("Ignoring file with extension %s", ext)
                    continue

                log.info("Full path: %s", full_path)
                log.info("Content dir: %s", content_dir)

                content_file = HugoContent(full_path, content_dir)
                content_files.append(content_file)

        log.info(extensions)
        return content_files


class CommandImportRgb(Command):
    """Import Hugo content from my site

    At some point maybe this can be refactored to a general Hugo import plugin.
    For now it tracks progress importing my specific setup into a new specific setup.
    """

    name = "import_rgb"
    doc_usage = "[options]"
    doc_purpose = "import my Hugo site"

    def _execute(self, options, args):
        """The plugin hook for running the import."""
        import_rgb_config_setting = self.site.config.get(HUGO_CONFIG_SETTING, None)

        if not import_rgb_config_setting:
            log.error("I need a setting for %s!", HUGO_CONFIG_SETTING)
            return 0

        rgb_config_path = Path(import_rgb_config_setting).expanduser()

        if not rgb_config_path.is_file():
            log.error(f"I can't find f{rgb_config_path}!")

        return self.import_using_config(rgb_config_path)

    def import_using_config(self, hugo_config):
        """The actual import process"""
        log.info(f"Using {hugo_config}")

        # collect all the filenames
        safe_extensions = (".md", ".rst", ".html")
        hugo_site = HugoSite(config_file=hugo_config, safe_extensions=safe_extensions)
        content_files = hugo_site.collect_content_files()
        # pages_dir = "pages"
        # posts_dir = "posts"
        # log.info(f"Removing {posts_dir}")
        # remove_file(posts_dir)

        for hugo_content in content_files:
            hugo_content.import_content()
