---
aliases:
- /tools/2014/06/22_what-is-build-essentials-for-opensuse.html
- /post/2014/what-is-build-essentials-for-opensuse/
categories:
- tools
date: 2014-06-22T00:00:00Z
tags:
- suse
title: What is build-essentials for openSUSE
type: post
year: '2014'
---
*TL;DR* `devel_basis`
<!--more-->

[build-essential]: http://packages.ubuntu.com/trusty/build-essential
[openSUSE]: http://opensuse.org
[devel_basis]: http://software.opensuse.org/package/patterns-openSUSE-devel_basis

This is the umpteenth time I looked up what [build-essential][] is on [openSUSE][].
For my purposes, it's the [devel_basis][] pattern.

To see what packages have the pattern,

~~~ console
$ zypper info -t pattern devel_basis
~~~ 

Yes it has a lot of packages, but I usually end up installing many of those anyways.

To install `devel_basis`,

~~~ console
$ sudo zypper install -t pattern devel_basis
~~~ 

That's all. I've started remembering to *use* the notes on my site, which 
means it occurs to me that more notes would be helpful.
