---
date: 2020-05-08 20:25:00-07:00
tags:
- IndieWeb
- data
- i fixed it!
- before I pushed it
- yay for tests
title: Debugging My Site With a Little Help From My Friends
slug: debugging-my-site-with-a-little-help-from-my-friends
uuid: 72e20ceb-c3da-47b3-9736-3c397bc63da5
category: note
type: micro
previewimage: /images/2020/05/debugging-my-site-with-a-little-help-from-my-friends/cover.png
---
{{< quote source="Me, a couple months ago" >}}
It’s probably redundant to test HTML structure for my pages, but [what
the heck](/note/2020/03/passing-tests-is-now-required-to-push).
{{< /quote >}}

{{< quote source="Me, a few weeks ago" >}}
There’s no rule, but *obviously* [every webmention to my
site](/note/2020/04/yay-i-added-mentions-and-replies) will have full
author info including photo.
{{< /quote >}}

{{< quote source="Me, this morning" >}}
Look honey I added Webmentions to my [Datasette
dashboard](/note/2020/05/datasette-sure-is-nifty/)\!
{{< /quote >}}

{{< quote source="Me, an hour ago" >}}
Sweet, jmac liked my
[mention](/note/2020/05/pondering-my-indieweb-guinea-pig)\! Wait why
are tests failing? Maybe check the dashboard?
{{< /quote >}}

{{< quote source="Me, a few minutes ago" >}}
I fixed it\!
{{< /quote >}}

The fix is reasonable defaults for response author info. I got other
fixes in mind, including a default "card" for anonymous response
authors. Also, inferring author info from source site. Thanks for the
help and the ideas, {{< card-link "jmac" >}}!