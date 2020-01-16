---
announcements:
  mastodon: https://hackers.town/@randomgeek/102153562058385171
  twitter: https://twitter.com/brianwisti/status/1132062293209092098
categories:
- tools
date: 2019-05-24T00:00:00Z
tags:
- shell
title: Pretty Print Terminal Files With Bat
year: '2019'
---


[`bat`][] is like a fancier `cat` for displaying file contents.

[`bat`]: https://github.com/sharkdp/bat

<!--more-->

My work routine lately includes automatic generation of SQL files for
database updates. That routine includes quickly skimming them to find obvious
errors. I wanted something quicker than reviewing them in my editor, but fancier
than the simple plain text of `cat`.

I have the [Pygments][] syntax highlighting library for [Python][] installed, so I
could use `pygmentize` piped to `less` for paging:

``` shell
$ pygmentize -g work.sql | less -NR
```

However, that is noticeably slow and most definitely not convenient.  Adding an
alias helped the convenience, but did nothing for the sluggishness.

[Pygments]: http://pygments.org/
[Python]: /tags/python

[`bat`][] provides what I need. It runs quick enough that I don't need to
think about it, highlights code, numbers lines, indicates git changes in the
margin, and feeds the result to `less` if there's more than you can display on
one screen.

[`bat`]: https://github.com/sharkdp/bat

Packages are available for several Linux distributions, or you can install it
via [Homebrew][] (reminder: Homebrew works on macOS *and* Linux these days).

[Homebrew]: https://brew.sh/

``` shell
$ brew install bat
```

****

Oh hey there's something about the [Nix][] package manager on the `bat`
README. Adding a [Taskwarrior][] item to check that out later.

****

[Nix]: https://nixos.org/nix/
[Taskwarrior]: /tags/taskwarrior

Sometimes I need to check the structure of files where whitespace matters:
tab-delimited files, Makefiles, Python, stuff like that. `bat -A` shows
whitespace and other non-printable characters displayed, though you lose syntax
highlighting.

{{< show-figure
    image="showing-whitespace.png"
    description="The site Makefile — oh look a trailing space!" >}}

## Plain Text

I enjoy the formatting conveniences from `bat` even when examining plain text
files.

{{< show-figure
    image="bat-plain-text.png"
    description="bat showing a plain text file" >}}

This is all I've needed `bat` for, but it's flexible enough to work into your
everyday shell just like `cat`. Check out the [README][] for ideas.

[README]: https://github.com/sharkdp/bat

