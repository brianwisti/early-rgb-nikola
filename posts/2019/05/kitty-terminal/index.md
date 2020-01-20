---
announcements:
  mastodon: https://hackers.town/@randomgeek/102167342505236721
  twitter: https://twitter.com/brianwisti/status/1132944399011405825
date: 2019-05-27T00:00:00Z
tags:
- shell
title: Kitty Terminal
updated: 2019-05-27T00:00:00Z
year: '2019'
category: tools
---


I installed the [kitty][] terminal emulator for font ligatures on Linux, but it does other stuff too.

[kitty]: https://sw.kovidgoyal.net/kitty/index.html

<!-- TEASER_END -->

[kitty][] is a fast terminal emulator for Linux and macOS. It includes many features, but the one
that interested me was support for [ligatures][] in code. Ligatures *basically* let you combine symbols,
characters, or graphemes to produce a single glyph with compressed meaning.

[kitty]: https://sw.kovidgoyal.net/kitty/index.html
[ligatures]: https://en.wikipedia.org/wiki/Typographic_ligature

{{< show-figure
    image="all_ligatures.png"
    description="Fira Code ligatures via [Github](https://github.com/tonsky/FiraCode/blob/master/showcases/all_ligatures.png)" >}}

Confused yet? Me too. I barely understand what I'm trying to describe here. Really it's just that ligatures
make your code look cooler than the plain text most developers enter and read for hours a day. Whether
they improve life in any meaningful fashion is arguable, but "it looks cooler" is good enough for me today.

By using a special font such as [Fira Code][] and a capable terminal, all sorts of character transformations
happen. For example, the `<` and `=` characters combined as `<=` — to indicate "less than or equal to" —
displays as `⩽`. It means the same thing, but it says it with a single visual character.

[Fira Code]: https://github.com/tonsky/FiraCode

We have this rich library of symbols to describe our solutions, but most programming languages use a tiny
subset of those symbols. Except Perl 6 of course. Perl 6 sort of does everything.

``` shell
$ perl6 -e 'say 1 ≤ 5'
True
```

Anyways, back to ligatures. They let you pretend you're using that rich library of symbols.

Gnome Terminal does not support ligatures, at least not on my system. Konsole from the [KDE][] project does,
but adds many KDE-specific dependencies to my system. I wanted to find something a bit more lightweight.

[KDE]: https://www.kde.org/

*kitty* satisfies that need.

## Installing *kitty*

*kitty* runs on both Linux and macOS, but right now I'm concerned with Linux. I already have [iTerm2][] for
ligatures on macOS.

[iTerm2]: https://iterm2.com/

The [installation instructions][] for *kitty* follow a familiar pattern of "grab and run the installer
script." If you don't feel safe with that you can [install from source][].

[installation instructions]: https://sw.kovidgoyal.net/kitty/binary.html
[install from source]: https://sw.kovidgoyal.net/kitty/build.html

``` shell
$ curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
```

`installer.sh` loads Python to download the latest *kitty* executable to `~/.local/kitty.app` on Linux.

I followed the installation instructions for desktop integration, making small adjustments as needed for my
own system setup.

``` shell
$ ln -s ~/.local/kitty.app/bin/kitty ~/bin/
$ cp ~/.local/kitty.app/share/applications/kitty.desktop \
  ~/.local/share/applications
$ sed -i \
  "s/Icon\=kitty/Icon\=\/home\/$USER\/.local\/kitty.app\/share\/icons\/hicolor\/256x256\/apps\/kitty.png/g" \
  ~/.local/share/applications/kitty.desktop
$ chmod u+x ~/.local/share/applications/kitty.desktop
```

These steps put *kitty* on my `$PATH` and create a desktop entry complete with application icon for launching
from the GNOME Menu.

My `kitty.desktop` file ended up looking like this after a couple edits
(specifying executable path, stuff like that).

```
[Desktop Entry]
Version=1.0
Type=Application
Name=kitty
GenericName=Terminal emulator
Comment=A fast, feature full, GPU based terminal emulator
TryExec=/home/randomgeek/bin/kitty
Exec=/home/randomgeek/bin/kitty
Icon=/home/randomgeek/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png
Categories=System;TerminalEmulator;
```

Course, I still had to tell GNOME the desktop launcher was trustworthy but
opening `/.local/share/applications/kitty.desktop` in the GNOME file manager.

{{< show-figure
    image="gnome-trust.png"
    description="GNOME dialog" >}}


## Font installation

I need a font that supports ligatures now. Fira Code is the one I know best, though I wouldn't mind
trying others. Fortunately, Fira Code is available via my system package manager.

``` shell
> sudo apt install fonts-firacode
```

## *kitty* configuration

Next step is to define my [configuration][] in `~/.config/kitty/kitty.conf`. The whole point of this
experiment is to get ligatures, so that's my first configuration change.

[configuration]: https://sw.kovidgoyal.net/kitty/conf.html


``` text
font_family           Fira Code
bold_font             auto
italic_font           auto
bold_italic_font      auto
font_size             14.0
```

Then throw in some window geometry stuff. Normally *kitty* remembers and applies the last window size you
used, but I often don't want that for the quick transient terminals I open during my day. Instead I go with a
terminal 110 characters wide and 40 columns tall.

``` text
remember_window_size  no
initial_window_width  110c
initial_window_height 40c
```

*kitty* does not load a login shell by default. I prefer a login shell, so I specify that in
`kitty.conf`.

``` text
shell                 /bin/bash --login
```

## Using *kitty*

{{< show-figure
    image="mojolicious.png"
    description="Ligatures when looking at Mojolicious source" >}}

The ligatures are pretty, of course. But what I really notice? Kitty is fast.
Maybe that's just because I became accustomed to GNOME Terminal and its
sluggishness. Kitty might not be [rxvt][] fast, but it's much quicker than what
I'm used to.

[rxvt]: http://rxvt.sourceforge.net/

Since kitty is a terminal emulator, most of the functionality is familiar. The
default [keyboard shortcuts][] are similar to those offered by GNOME Terminal,
with support for clipboard access and tabs. *kitty* also supports windows much
like panes in [tmux][], but for now I'm sticking with the familiarity of tmux.

[keyboard shortcuts]: https://sw.kovidgoyal.net/kitty/index.html#tabs-and-windows
[tmux]: https://github.com/tmux/tmux/wiki

## Speaking of tmux

terminfo should install what's needed, but if not you will see an annoying message when you try to start tmux:

``` shell
open terminal failed: missing or unsuitable terminal: xterm-kitty
```

This works:

``` shell
$ TERM="xterm-256color" tmux
```

But see [here](https://unix.stackexchange.com/questions/470676/tmux-under-kitty-terminal) for better
instructions. Or at least a pointer to better instructions.

## kittens

[Kittens][] are Python scripts that take advantage of features provided by kitty.
Kitty includes built-in kittens for handling [handling arbitrary text][] such as
URLs, working with the [clipboard][], and viewing [file diffs][]. You can even
[write your own][]!

[Kittens]: https://sw.kovidgoyal.net/kitty/index.html#kittens
[handling arbitrary text]: https://sw.kovidgoyal.net/kitty/kittens/hints.html
[clipboard]: https://sw.kovidgoyal.net/kitty/kittens/clipboard.html
[file diffs]: https://sw.kovidgoyal.net/kitty/kittens/diff.html
[write your own]: https://sw.kovidgoyal.net/kitty/kittens/custom.html

Most of the kittens are useful, but a couple also make for great screenshots. So
here they are 😸

### icat

[icat][] shows an image in the terminal.

[icat]: https://sw.kovidgoyal.net/kitty/kittens/icat.html

``` shell
$ kitty +kitten icat cat-fall.jpeg
```

{{< show-figure
    image="kitty-icat.png"
    description="classic cat pics in the terminal!" >}}

****

Over on Twitter, [Yanick Champoux][] noted that `icat` does not play well
with tmux.

{{< tweet 1133131184089681920 >}}

Confirmed for myself by running `icat` in a tmux window.

``` shell
$ kitty +kitten icat content/post/2019/kitty-terminal/kitty-icat.png 
Terminal does not support reporting screen sizes via the TIOCGWINSZ ioctl
```

Dang. Thanks, Yanick!

****

[Yanick Champoux]: http://techblog.babyl.ca/

### Unicode Input

`Control-Shift-U` lets you enter [Unicode characters][], by code or by name.

[Unicode characters]: https://sw.kovidgoyal.net/kitty/kittens/unicode-input.html

{{< show-figure
    image="unicode-entry.png"
    description="Entering a unicode character by name in kitty" >}}

## kitty is fun

Even if I get tired of ligatures — a distinct possibility — I can see continuing
to use kitty for its speed and extensibility. Anyways, it's fun to expand my
toolkit a little more!

