---
announcement: In which I spent Sunday having fun learning stuff
announcements:
  mastodon: https://hackers.town/@randomgeek/102759304764890808
  twitter: https://twitter.com/brianwisti/status/1170830219390963713
date: 2019-09-08
tags:
- go
- shell
title: Colorized my go output with grc
year: '2019'
category: tools
previewimage: /images/2019/09/colorized-my-go-output-with-grc/cover.png
---

[Go]: https://golang.org/
[Learn Go with Tests]: https://github.com/quii/learn-go-with-tests
[official tour]: https://tour.golang.org/welcome/1
[Chris James]: https://quii.dev/
[Stack Overflow answer]: https://stackoverflow.com/a/40160711

Enjoying myself as I go through [Learn Go with Tests][] by [Chris James][].

I didn't enjoy myself on the [official tour][], or with whatever LinkedIn course it was that I took. The
structure and flow of the learn-by-testing piece gives me a familiar context and the pace seems just about
right. It's giving me ideas where I might enjoy Go for my own projects.

So yeah I like it.

Still having some *tiny* issues with the output of `go test`.

{{< show-figure
  image="plain.png"
  description="normal `go test` output" >}}

Part of it's that my brain hasn't gotten used to how Go displays its errors. Some of it's that my brain always
has --- and always will --- panic at random symbols without context.

I figured I wasn't the first with this problem, so I went looking. Found a [Stack Overflow answer][] pointing
me to [grc][]. Installed via [Homebrew][], then followed directions from Stack Overflow to configure grc, with
a slight tweak to `~/.grc/conf.gotest`.

[grc]: https://github.com/garabik/grc
[Homebrew]: https://brew.sh/

grc needs an entry in `~/.grc/grc.conf` for Go test runs.

```
# Go
\bgo.* test\b
conf.gotest
```

I did make a slight tweak to the suggested `~/.grc/conf.gotest`, so that "panic" lines get highlighted as failures.

```
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
```

Now when I run tests through `grc go test`, output is colorized and I can track it more easily!

Of course I'll probably get used to how Go presents errors and then forget all about [grc][], but it's great
for today. Might be more generally useful too, if I want colorized output that my tools don't already provide!
