#!/usr/bin/env python

"""Import Hugo content, generating metadata and converting as necessary"""

import logging
import os

from nikola.plugin_categories import Command
from nikola.utils import copy_file, makedirs

log = logging.getLogger(os.path.basename(__file__))
HUGO_CONFIG_SETTING = "IMPORT_RGB_CONFIG"

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

        return self.import_using_config(import_rgb_config_setting)


    def import_using_config(self, hugo_config):
        """The actual import process"""
        rgb_config = os.path.expanduser(hugo_config)

        if not os.path.exists(rgb_config):
            log.error(f"Missing {rgb_config}?")
            return 0

        log.info(f"Using {rgb_config}")

        # collect all the filenames
        safe_extensions = (".md",)
        extensions = {}
        site_dir = os.path.dirname(rgb_config)
        content_dir = os.path.join(site_dir, "content/post/")
        posts_dir = "posts"

        log.info(f"site_dir: {site_dir}")
        log.info(f"content_dir: {content_dir}")

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

                if ext not in safe_extensions:
                    # Dunno how to handle it yet.
                    continue

                extensions[ext] = extensions.get(ext, 0) + 1
                log.info(full_path)
                hugo_path = full_path.replace(content_dir, "")
                log.info(hugo_path)
                log.info(f"hugo_path: {hugo_path}")
                nikola_path = os.path.join(posts_dir, hugo_path)
                log.info(f"nikola_path: {nikola_path}")
                nikola_dir = os.path.dirname(nikola_path)
                log.info(f"post will go in {nikola_dir}")
                copy_file(full_path, nikola_dir)

        log.info(extensions)
