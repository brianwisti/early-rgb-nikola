#!/usr/bin/env python

"""Import Hugo content, generating metadata and converting as necessary"""

from dataclasses import dataclass
import os
from typing import List, Tuple

from nikola.plugin_categories import Command
from nikola.utils import copy_file, get_logger, makedirs, remove_file

log = get_logger(os.path.basename(__file__))
HUGO_CONFIG_SETTING = "IMPORT_RGB_CONFIG"

@dataclass
class HugoSite:
    """Knows enough about a Hugo site to help import its content into Nikola"""
    config_file: str
    safe_extensions: Tuple[str]
    
    def collect_content_files(self) -> List[str]:
        """Return a list of files in the Hugo site that are safe for import"""
        site_dir = os.path.dirname(self.config_file)
        content_dir = os.path.join(site_dir, "content/post/")
        content_files = []
        extensions = {}

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

                content_files.append(full_path)

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
            log.info(hugo_content_file)
            content_path = hugo_content_file.replace(content_dir, "")
            nikola_path = os.path.join(posts_dir, content_path)
            copy_file(hugo_content_file, nikola_path)
