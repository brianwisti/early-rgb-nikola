---
slug: colorized-my-go-output-with-grc
description: In which I spent Sunday having fun learning stuff
date: 2019-09-08
tags:
- go
- shell
- tools
title: Colorized my go output with grc
uuid: 9cff48b0-9ca3-416b-a52d-a1c2f377d21e
aliases:
- /2019/09/08/colorized-my-go-output-with-grc/
previewimage: /images/2019/09/colorized-my-go-output-with-grc/cover.png
---
Enjoying myself as I go through [Learn Go with
Tests](https://github.com/quii/learn-go-with-tests) by [Chris
James](https://quii.dev/).

I didn’t enjoy myself on the [official
tour](https://tour.golang.org/welcome/1), or with whatever LinkedIn
course it was that I took. The structure and flow of the
learn-by-testing piece gives me a familiar context and the pace seems
just about right. It’s giving me ideas where I might enjoy Go for my own
projects.

So yeah I like it.

Still having some *tiny* issues with the output of `go test`.

![normal `go test` output](plain.png)

Part of it’s that my brain hasn’t gotten used to how Go displays its
errors. Some of it’s that my brain always has — and always will — panic
at random symbols without context.

I figured I wasn’t the first with this problem, so I went looking. Found
a [Stack Overflow answer](https://stackoverflow.com/a/40160711) pointing
me to [grc](https://github.com/garabik/grc). Installed via
[Homebrew](https://brew.sh/), then followed directions from Stack
Overflow to configure grc, with a slight tweak to `~/.grc/conf.gotest`.

grc needs an entry in `~/.grc/grc.conf` for Go test runs.

    # Go
    \bgo.* test\b
    conf.gotest

I did make a slight tweak to the suggested `~/.grc/conf.gotest`, so that
"panic" lines get highlighted as failures.

    regexp==== RUN .*
    colour=blue
    -
    regexp=--- PASS: .*
    colour=green
    -
    regexp=^PASS$
    colour=green
    -
    regexp=^(ok|\?) .*
    colour=magenta
    -
    regexp=^\s*panic: .*
    colour=red
    -
    regexp=--- FAIL: .*
    colour=red
    -
    regexp=[^\s]+\.go(:\d+)?
    colour=cyan

Now when I run tests through `grc go test`, output is colorized and I
can track it more easily\!

![colorized by `grc go test`](cover.png)

Of course I’ll probably get used to how Go presents errors and then
forget all about [grc](https://github.com/garabik/grc), but it’s great
for today. Might be more generally useful too, if I want colorized
output that my tools don’t already provide\!