---
title: SSG is for putterers
slug: ssg-is-for-putterers
date: 2020-09-20 10:29:56-07:00
tags:
- ssg
- blogging
- puttering
- indieweb
category: note
type: micro
---
{{< reply-context
  in-reply-to="https://kevq.uk/wordpress-creator-vs-the-jamstack/"
  title="WordPress Creator Vs The Jamstack"
  published="2020-05-20"
  author="Kev Quirk"
  summary="Kev Quirk on static site generators"
>}}
SSGs are really cool and super fun to play with – I’m really enjoying it on my side project; but
I wish a lot of devs would stop touting about how amazingly simple they are, as it’s just not the case.
{{< /reply-context >}}

I often see "such and such static site generator is simple!" tweets, and wonder what exactly they're
comparing it to. DIY dentistry perhaps?

[some SSGs]: https://www.11ty.dev/

As much as I love puttering with static site generators, "puttering" is the main charm of an SSG.
The hooks to customize are right there on the surface. Heck [some SSGs][] are nothing *but* hooks. And
having everything in a git repository is just a developer-focused version of a smart backup plan.

[webmention.io]: https://webmention.io/
[Jamstack]: https://jamstack.org/

For the [Jamstack][] side of things, I'm not sure I see the advantage of relying on a load of external
services over oh say for example having a database and an internal comment system. You know, like
Wordpress. Something I've been thinking about a lot in relation to my own site leaning so much on
[webmention.io][].