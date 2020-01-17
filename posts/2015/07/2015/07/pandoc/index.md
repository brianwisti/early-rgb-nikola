---
aliases:
- /tools/2015/07/23_pandoc.html
- /post/2015/pandoc/
date: 2015-07-23T00:00:00Z
tags:
- pandoc
title: Pandoc
type: post
year: '2015'
category: tools
---
[Pandoc]: http://pandoc.org/
I could use [Pandoc][] to build HTML from my site sources.
<!--more-->

I could use it to convert them to different sources.

I'm not saying I *would*. But I *could*.

Okay I might.

    $ pandoc --to org _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.org
    $ pandoc --to asciidoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.adoc
    $ pandoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.html

{{< show-figure image="emacs-pandoc.png" description="Pandoc output in Emacs" >}}

Honestly at this point I'd say it's pretty likely.
