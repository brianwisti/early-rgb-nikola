#!/usr/bin/env python

"""Import Hugo content, generating metadata and converting as necessary"""

from dataclasses import dataclass, field
import os
import re
from typing import Any, Dict, List, Tuple

from nikola.plugin_categories import Command
from nikola.utils import copy_file, get_logger, makedirs, remove_file, slugify
from ruamel.yaml import YAML

log = get_logger(os.path.basename(__file__))
yaml = YAML()
HUGO_CONFIG_SETTING = "IMPORT_RGB_CONFIG"

@dataclass
class HugoContent:
    """Knows enough about a Hugo content file to help import itself into Nikola"""
    hugo_file: str
    content_dir: str
    frontmatter: Dict[str, Any] = field(init=False)
    content: str = field(init=False)
    is_post: bool = field(init=False)

    def __post_init__(self):
        delimiter = "---\n"
        _, yaml_text, body_text = open(self.hugo_file).read().split(delimiter, maxsplit=2)
        self.content = body_text
        yaml_text = re.sub(r"^(date: \d{4}-\d{2}-\d{2})T", r"\1 ", yaml_text)
        self.frontmatter = yaml.load(yaml_text)

        date = self.frontmatter.get("date", None)

        if date:
            self.is_post = True
        else:
            self.is_post = False
    
    def preferred_path(self):
        """My location in the nikola site"""
        _, ext = os.path.splitext(self.hugo_file)
        date_path = self.frontmatter["date"].strftime("%Y/%m")
        title_path = slugify(self.frontmatter["title"])
        base_path = f"index{ext}"
        return os.path.join(date_path, title_path, base_path)


@dataclass
class HugoSite:
    """Knows enough about a Hugo site to help import its content into Nikola"""
    config_file: str
    safe_extensions: Tuple[str]
    
    def collect_content_files(self) -> List[HugoContent]:
        """Return a list of files in the Hugo site that are safe for import"""
        site_dir = os.path.dirname(self.config_file)
        content_dir = os.path.join(site_dir, "content")
        content_files = []
        extensions: Dict[str, int] = {}

        for root, dirs, files in os.walk(content_dir):
            for filename in files:
                if filename.startswith("_"):
                    # leading underscores are for section summaries.
                    continue

                if filename.endswith("~"):
                    # A backup file got in there somehow.
                    continue

                full_path = os.path.join(root, filename)
                _, ext = os.path.splitext(filename)

                extensions[ext] = extensions.get(ext, 0) + 1

                if ext not in self.safe_extensions:
                    # Dunno how to handle these
                    continue

                content_files.append(HugoContent(hugo_file=full_path, content_dir=content_dir))

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
            log.error(f"I need a setting for {HUGO_CONFIG_SETTING}!")
            return 0
        
        rgb_config_path = os.path.expanduser(import_rgb_config_setting)

        if not os.path.exists(rgb_config_path):
            log.error(f"I can't find f{rgb_config_path}!")

        return self.import_using_config(rgb_config_path)


    def import_using_config(self, hugo_config):
        """The actual import process"""
        log.info(f"Using {hugo_config}")

        # collect all the filenames
        safe_extensions = (".md", ".rst", ".adoc", ".html")
        hugo_site = HugoSite(config_file=hugo_config, safe_extensions=safe_extensions)
        log.info(hugo_site)
        content_files = hugo_site.collect_content_files()
        site_dir = os.path.dirname(hugo_config)
        content_dir = os.path.join(site_dir, "content/post/")
        posts_dir = "posts"
        log.info(f"Removing {posts_dir}")
        remove_file(posts_dir)

        log.info(f"site_dir: {site_dir}")
        log.info(f"content_dir: {content_dir}")

        for hugo_content_file in content_files:
            log.info(hugo_content_file.hugo_file)
            if hugo_content_file.is_post:
                content_path = hugo_content_file.preferred_path()
                # TODO: Use NEW_POST_DATE_PATH_FORMAT, if NEW_POST_DATE_PATH is True
                nikola_path = os.path.join(posts_dir, content_path)
                log.info(f"{hugo_content_file.frontmatter['title']} -> {nikola_path}")
                copy_file(hugo_content_file.hugo_file, nikola_path)
