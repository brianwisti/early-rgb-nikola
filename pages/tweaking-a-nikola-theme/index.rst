---
title: Tweaking a Nikola Theme
year: '2020'
draft: true
tags:
- nikola
- site
category: tools
previewimage: /images/tweaking-a-nikola-theme/cover-in-post.png
---

.. _Nikola: https://getnikola.com

Adjusting the default Nikola_ theme to show cover images
.. TEASER_END

.. contents::

Motivation
==========

I am a visual person.
You might not know that from all the typing and my enthusiasm for command line tools.
But many of my posts and pages have cover images.
Sometimes the cover images are even relevant to the post.

In the live site, cover images are prominently displayed at the top of their pages.
They get referenced when a post gets shared on social media.
A cropped and adjusted version of the cover image gets displayed in post summaries.

So if I'm using `Nikola`_ to build something like my current site, I need to get cover images.

.. _bootblog4: https://themes.getnikola.com/v8/bootblog4/

A default Nikola site uses the `bootblog4`_ theme.
bootblog4 doesn't support cover images, so I'll make a version that does.

I don't want to build a whole new theme.
Not yet, anyways.
I just want to tweak the default a little.

Prelude
=======

Nikola starts with a few assumptions I can work with.
bootblog4 already looks for ``previewimage`` metadata to build thumbnails for `featured posts`.
Image files go in your site's ``images/`` folder.

.. _a recent note:
.. _that post: {{< ref "note/2019-12-15-1237/index.md" >}}

Makes sense.
I'll mirror the content path with images.
The cover image for `a recent note`_ goes in ``images/2019/12/again-with-the-manual-symmetry/cover.jpg``.

.. note::

  I like how Hugo handles page bundles.
  Everything for your content is in the same folder.
  Most other static site generators —
  including Nikola —
  keep supplemental content separate from posts.

Directions
==========

`Hugo` uses its powerful but sometimes confusing `taxonomy` system in layout customization.
`Nikola` prefers a powerful but sometimes confusing `theme inheritance` system.
Look.
They're all confusing.
It's just a matter of finding the kind of confusing you don't mind.

With theme inheritance, my tweaks *are* a new theme.
But the new theme basically says "I'm like that theme, except for these templates."

So let's inherit a theme.

Nikola's ``theme`` command
--------------------------

-i ARG, --install=ARG        Install a theme.
                             (config: install)
-r ARG, --uninstall=ARG      Uninstall a theme.
                             (config: uninstall)
-l, --list                   Show list of available themes.
                             (config: list)
--list-installed             List the installed themes with their location.
                             (config: list_installed)
-u ARG, --url=ARG            URL for the theme repository
                             (default: https://themes.getnikola.com/v8/themes.json)
                             (config: url)
-g ARG, --get-path=ARG       Print the path for installed theme
                             (config: getpath)
-c ARG, --copy-template=ARG  Copy a built-in template into templates/ or your theme
                             (config: copy-template)
-n ARG, --new=ARG            Create a new theme
                             (config: new)
--engine=ARG                 Engine to use for new theme
                             (mako or jinja -- default: mako)
                             (config: new_engine)
--parent=ARG                 Parent to use for new theme
                             (default: base)
                             (config: new_parent)
--legacy-meta                Create legacy meta files for new theme
                             (config: new_legacy_meta)

.. _option-list: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists

.. note:: built with RST's handy-dandy `option-list`_

So I need a new theme, using bootblog4 as the parent.

.. code:: shell-session

  $ nikola theme --new rgb-bootblog4 --parent bootblog4
  ...
  [2020-01-21T15:35:33Z] NOTICE: theme: Remember to set THEME="rgb-bootblog4" in conf.py to use this theme.

I didn't specify a template engine, so rgb-bootblog4 uses Mako_.

Update ``conf.py`` as directed.
The `theme tutorial` also mentions disabling ``PAGE_BUNDLES``.

.. code:: python

  # Name of the theme to use.
  THEME = "rgb-bootblog4"
  …
  USE_BUNDLES = False

Sweet.
I have a new ``themes/rgb-bootblog4`` folder.
Wait.
It has no templates.

Ah, I see.
This is what they were talking about with *template inheritance*.
The templates are still in the parent. It's up to me to copy and change the specific templates.
That's both good and a little risky when the parent theme updates.
What if my tweak turns out to be incompatible?
Okay, not going to worry about it today.
If you're going to veer wildly from the parent, you should probably use "base" as the parent.

Adding cover images to posts
----------------------------

So which template do I want?
Both pages and posts may have a cover image, so something more general.

.. code:: shell-session

   $ nikola theme -c base.tmpl

Over here on the live site, I put cover images above the main content.
Can I find anything interesting in the base template?

.. topic:: base.tmpl

  .. code:: mako
    :number-lines: 70

     ${template_hooks['page_header']()}
     <%block name="extra_header"></%block>
     <%block name="content"></%block>

.. tip::

  The `Mako` extension for `Visual Studio Code` associates itself with ``.mako`` files.
  You can add ``.tmpl`` to that with the `files.associations` setting.
  Might not want to do that globally though.
  ``.tmpl`` could be Mako here, but Jinja2 in another site.

  Instead, change it in the workspace file for your Nikola site.

  .. code:: json

    {
      "folders": [
        {
          "path": "."
        }
      ],
      "settings": {
        "files.associations": {
          "*.tmpl": "mako"
        }
      }
    }

``extra_header`` looks promising.
Pages ultimately inherit from posts —
Mako supports `template inheritance` —
so we might be able to do this with one change.

.. code:: shell-session

  $ nikola theme -c post.tmpl

.. topic:: post.tmpl

  .. code:: mako
    :number-lines: 30

      <%block name="extra_header">
        % if post and post.previewimage:
            <div class="figure">
                <img src="${post.previewimage}" alt="${post.title}" width="1000">
                <p class="caption">${post.title()}</p>
            </figure>
        % endif
    </%block>

Keep in mind what I noticed `the other day` about these not being real figures in reStructuredText.
For now I match the RST output.
That way I don't have to find the CSS for this theme.

{{< show-figure image="cover-in-post.png"
  description="Cover image in a post" >}}

It has a cover image, placed right by the title.
It doesn't *quite* match today's view of `that post`_.
But this gets the effect across while only editing a single template file.

{{< show-figure image="post-hugo-comparison.png"
  description="the same post on the live site" >}}

Looks good for posts that have a cover image.
How about pages?

{{< show-figure image="cover-in-page.png"
  description="Cover image in a page" >}}

Excellent.
I thought that would take much more work.

Resources
=========

- https://getnikola.com/theming.html
- https://getnikola.com/theming.html#built-in-templates
- https://getnikola.com/creating-a-theme.html
- https://getnikola.com/template-variables.html

.. _Mako: https://www.makotemplates.org/
.. _Jinja2: https://jinja.palletsprojects.com/
