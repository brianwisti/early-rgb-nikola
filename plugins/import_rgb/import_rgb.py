#!/usr/bin/env python

"""Import Hugo content, generating metadata and converting as necessary"""

import os

from nikola.plugin_categories import Command


class CommandImportRgb(Command):
    """Import Hugo content from my site"""

    name = "import_rgb"
    doc_usage = "[options]"
    doc_purpose = "import my Hugo site"

    def _execute(self, options, args):
        """Run the import."""
        rgb_config = os.path.expanduser(self.site.config["IMPORT_RGB_CONFIG"])

        if not os.path.exists(rgb_config):
            print(f"Error: Missing {rgb_config}?")
        else:
            print(f"Using {rgb_config}")

