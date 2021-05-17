---
title: Every Post Has a UUID
slug: every-post-has-a-uuid
uuid: cbb6a258-26a8-40fb-ac13-882c3ab2a52b
date: 2020-03-21 19:06:00-07:00
tags:
- site
- helpful hint
aliases:
- /note/2020/81/every-post-has-a-uuid/
category: note
type: micro
---
Gave them all a Universally Unique Identifer, per
[RFC 4122](http://www.faqs.org/rfcs/rfc4122.html).

Should simplify rearranging the site sources. Helpful hint: don’t rely
on filenames as unique content identifiers for your workflow. Oh sure
they work fine 80% of the time, but that last 20% is a doozy.

I used Python’s [uuid](https://docs.python.org/3/library/uuid.html)
library. There’s also the
[uuidgen](http://bigdatums.net/2016/10/01/generate-uuid-linux/) command
if I switch away from a Python workflow.