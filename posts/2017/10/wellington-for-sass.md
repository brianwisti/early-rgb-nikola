---
announcements:
  twitter: https://twitter.com/brianwisti/status/925593674230112256
categories:
- tools
date: 2017-10-31T00:00:00Z
draft: false
tags:
- site
- css
title: Wellington for Sass
year: '2017'
---
I found [Wellington][], a [Sass][] compiler written in [Go][].

[Wellington]: https://getwt.io/
[Sass]: http://sass-lang.com/
[Go]: https://golang.org/
<!--more-->

I installed Wellington with [Homebrew][] - actually [Linuxbrew][] but that's a post for another day maybe,
once I'm sure this Linuxbrew experiment worked for me.

[Linuxbrew]: http://linuxbrew.sh/
[Homebrew]: https://brew.sh/

``` console
$ brew install wellington
```

This is not the night to redesign the whole site, though. Make sure everything works.

``` console
$ wt compile assets/scss/main.scss -b static/css
2017/10/31 21:09:54 Compilation took: 28.333622ms
```

Seems to produce the same style output. I had no complaint about the speed of Ruby's Sass compiler, but Wellington is
certainly quicker.

I guess now I can start thinking about redesigning the site layout.
