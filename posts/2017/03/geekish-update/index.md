---
aliases:
- /post/2017/geekish-update/
announcements:
  twitter: https://twitter.com/brianwisti/status/846963326718480384
date: 2017-03-28T00:00:00Z
draft: 'false'
tags:
- personal
- site
title: Geekish Update
year: '2017'
category: marginalia
---
I set up a space for myself in the basement. This is now where I keep my desktop - running [Ubuntu][] at the
moment. Easy enough to get at from the laptop upstairs. Maybe keep [Irssi][] running in a [Tmux][] session or
something.

[Tmux]: https://tmux.github.io/
[Irssi]: https://irssi.org/
[Ubuntu]: https://www.ubuntu.com/
<!-- TEASER_END -->

Oh, and just in case you want to know how the basement looked when we moved in, here's a picture.

{{< show-figure image="basement-original.jpg" description="The original basement" >}}

I like it better now.

What have I been coding in this workspace that looks a bit less like a horror movie scene than it did a few
weeks ago?

I'm working on a `test` rule for this site. Mainly I use it to check for bad links in an attempt to deal with
[link rot][]. The link checker is [Python][] with [Requests][], and seeing if [Scrapy][] can be useful in this context. Scrapy
seems like overkill at first glance, but it has middleware for respecting [robots.txt][]. I care about being a
good Internet citizen.

I plan to write about that soon, since I enjoy the task so far.

[link rot]: https://en.wikipedia.org/wiki/Link_rot
[Python]: https://www.python.org/
[Requests]: http://docs.python-requests.org/en/master/
[Scrapy]: https://scrapy.org/
[robots.txt]: http://www.robotstxt.org/
