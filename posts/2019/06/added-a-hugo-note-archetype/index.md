---
aliases:
- /note/2019/0003/
announcements:
  mastodon: https://hackers.town/@randomgeek/102324468805367109
  twitter: https://twitter.com/brianwisti/status/1143000378511941632
date: 2019-06-23T19:55:11-07:00
tags:
- notes
- hugo
- posted from my phone
- sort of
- mobile hotspot
- my data usage is gonna hurt
title: Added a Hugo note archetype
year: '2019'
---

Moved into a new apartment. Waiting for Internet on Tuesday. It's Sunday.

Continuing to work slow but sure on my [notes][] experiment. Today: a Hugo
[archetype][] that includes a full [ISO 8601][] timestamp, via [`dateFormat`][].

[notes]: /note
[archetype]: https://gohugo.io/content-management/archetypes/
[ISO 8601]: https://en.wikipedia.org/wiki/ISO_8601
[`dateFormat`]: https://gohugo.io/functions/dateformat

    ---
    date: "{{ dateFormat "2006-01-02T15:04:05-07:00" .Date }}"
    hashtags:
    -
    ---

    SAY SOMETHING

And yeah, [hashtags][] are related to but distinct from [tags][]. Basically,
I have a particular protocol for tags and posts. I can be more informal
with notes and hashtags. The silly name reminds me they're supposed to be fun.

Working out the occasional overlap is a pending item in [Taskwarrior].

[hashtags]: /hashtags
[tags]: /tags
[Taskwarrior]: /tags/taskwarrior
