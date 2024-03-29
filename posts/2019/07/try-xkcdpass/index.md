---
slug: try-xkcdpass
description: In which I suggest a password generator
caption: '[XKCD 936](https://xkcd.com/936/) _([CC BY-NC 2.5](https://xkcd.com/license.html))_'
date: 2019-07-30 07:36:11-07:00
tags:
- linux
- security
- tools
title: Try xkcdpass
uuid: 4d3f885d-bec6-4096-b67b-2aaf31d97fa9
aliases:
- /2019/07/30/try-xkcdpass/
previewimage: /images/2019/07/try-xkcdpass/cover.png
---
*tl;dr*: Use [`xkcdpass`][] to generate more secure passwords, like
"correcthorsebatterystaple".

<!-- TEASER_END -->

<aside>Started as a <a href="/note/">Note</a> but I passed my 15 minute rule
— if I spend more than 15 minutes on it, it should be a post — so here we
are.</aside>

It won't satisfy your bank's silly password requirements, but --- as [XKCD told
us][] --- using a random collection of words for your password provides more security than
trying to [Leet-speak][] some word with numbers and symbols.

[XKCD told us]: https://xkcd.com/936/
[Leet-speak]: https://simple.wikipedia.org/wiki/Leet

You could pick a handful of words by flipping through the dictionary, but why not let the computer do it for you? That's where [`xkcdpass`][] comes in.

It's probably available in your package repository.

[`xkcdpass`]: https://pypi.org/project/xkcdpass/

    $ pacman -Ss xkcdpass

It's just [Python][], so you can use `pip` if you're on macOS or Windows or some other
platform that doesn't have `xkcdpass` handy.

[Python]: /tags/python

    $ pip install xkcdpass

Regardless of how you install it, run it and grab the output — but let your password manager remember it for
you.

    $ xkcdpass
    tiara embezzle stack doorway scrambled imitate