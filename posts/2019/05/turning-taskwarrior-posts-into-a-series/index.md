---
announcements:
  mastodon: https://hackers.town/@randomgeek/102082058493417205
  twitter: https://twitter.com/brianwisti/status/1127486161340063745
categories:
- Tools
date: 2019-05-12T00:00:00Z
tags:
- taskwarrior
- hugo
- site
title: Turning Taskwarrior Posts Into a Series
year: '2019'
---

There's a new taxonomy for posts that are written in a particular order!
<!--more-->

I want to more clearly show relations between some of my posts. Tags and
categories do handle a lot, but they get a bit clunky with stuff like my
[Taskwarrior][] posts, which specifically build on each other.

[Taskwarrior]: /tags/taskwarrior

[Hugo][] supports series as a taxonomy. Let's find out what that means.

[Hugo]: /tags/hugo

## Update site config

Even though Hugo pays attention to `series` for internal templates, it doesn't
count it towards taxonomies. So let's add an entry for it in site config.

``` toml
[taxonomies]
  # ...
  series = "series"
```

Now every post can be associated with zero or more series, and Hugo will notice.

## Update front matter

Add a `series` array with one entry for all of the
Taskwarrior posts so far (but not this one, since it isn't part of the series).

``` yaml
series:
- Taskwarrior Babysteps
```

## Create a series summary page

Oh look, there it is, already sitting at [`/series`][], thanks to my existing
`layouts/_default/terms.html`.

[`/series`]: /series

{{< show-figure
  image="series-listing.png"
  description="Listing of all series, currently just Taskwarrior Babysteps" >}}

What if I follow the link to [`/series/taskwarrior-babysteps`][]?

[`/series/taskwarrior-babysteps`]: /series/taskwarrior-babysteps

{{< show-figure
  image="taskwarrior-series-initial.png"
  description="The Taskwarrior Babysteps series listing" >}}

*Almost* perfect. But since each post is supposed to build on the others, I'd
prefer the listing present its posts in chronological order. I'll add
`layouts/series/series.html`.

``` go-html-template
{{ define "main" }}
  <h1>{{ .Title }}</h1>
  {{- .Content -}}
  {{ partial "term-path" . }}
  <ul class="post-list">
    {{- range .Pages.ByDate -}}
      <li class="post-list-item">
        {{- .Render "li" -}}
      </li>
    {{- end -}}
  </ul>
{{ end }}
```

And while I'm at it, how about an introduction to the series? I should be able
to put that at `content/series/taskwarrior-babysteps/_index.md`.

``` markdown

