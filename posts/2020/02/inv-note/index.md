---
title: inv note
slug: inv-note
caption: I drew this with [Amaziograph](https://amaziograph.com/)
date: 2020-02-05 07:54:39-08:00
tags:
- site
- pyinvoke
- drawing
- amaziograph
- fun
uuid: 0958cf9c-d72c-4ef3-bbc3-d36632f5bbc2
aliases:
- /note/2020/36/inv-note/
category: note
type: micro
previewimage: /images/2020/02/inv-note/cover.jpg
---
{{< console >}}
$ inv note --title='inv note'
{{< /console >}}

Don’t mind me. I’m just trying an experiment with using
[Invoke](https://docs.pyinvoke.org) for my site workflow instead of
[Make](https://www.gnu.org/software/make/).

{{< console >}}
$ inv serve
SHOW_INFO=1 hugo server --buildDrafts --bind 0.0.0.0 --navigateToChanged
...
Press Ctrl+C to stop
{{< /console >}}

But that’s boring on its own. Here. Have a drawing.

I’ll probably make a proper blog post about Invoke later. Meanwhile,
checkout the docs on [Getting
started](https://docs.pyinvoke.org/en/stable/getting-started.html).

{{< console >}}
$ inv publish
{{< /console >}}