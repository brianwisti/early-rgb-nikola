---
announcements:
  mastodon: https://hackers.town/@randomgeek/102818332962454350
date: 2019-09-19T01:43:31-07:00
tags:
- hugo
- oops
title: I FIXED MY .Pages
year: '2019'
category: note
---

Too tired to make it make sense. My site broke under Hugo .58. No front page listing. I fixed it. Yay!

Instead of (for notes):

```
{{- range first 1 (where .Pages "Section" "note") -}}
```

I used

```
{{- range first 1 (where .Site.RegularPages "Section" "note") -}}
```

I also fixed the RSS feed, and updated the [feeds post][] with those (very similar) details.

[feeds post]: {{< ref "post/2017/full-content-hugo-feeds.md" >}}
