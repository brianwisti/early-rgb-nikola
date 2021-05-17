---
title: Hugo Breadcrumbs
description: Finally
caption:
draft: true
tags:
- hugo
- tools
date: 2021-05-17
---
# Breadcrumbs?

[Smashing Magazine]: https://www.smashingmagazine.com/2009/03/breadcrumbs-in-web-design-examples-and-best-practices/

That trail at the top of the page.
It gives you links to each intermediate step on the path to this file.
It can be a useful way to show a narrowing of focus.
You don't see them *as* much on blogs, but I still like them.
[Smashing Magazine][] has a nice reference on the subject.

# Okay, but how?

Use subsection indexes. See, my content — most importantly, my dated content — is finally organized coherently.

Entry bundles — the content and any supplemental files — go in their own directory, which goes in a folder for the month published, which goes in a folder for the year published, which goes in the section.

![content path to this post](content-layout.png)

Citations needed:

- https://discourse.gohugo.io/t/solved-loop-through-subsections-posts/10526
- https://github.com/bep/hugotest/blob/master/layouts/partials/sections-tree.html

## The breadcrumb template

I need a good spot for the breadcrumb trail.
For now, the big site logo goes away and the breadcrumbs take its place.

{{< code file="layouts/_default/baseof.html" >}}
<header class="site-header">
  {{ partial "breadcrumb" . }}
  {{ partial "site-menu" . }}
</header>
{{< /code >}}

[breadcrumb example]: https://gohugo.io/content-management/sections/#example-breadcrumb-navigation

Even with my adjustments, this is pretty much the same template as the Hugo documentation [breadcrumb example][].

{{< code file="layouts/partials/breadcrumb.html" >}}
<ul  class="breadcrumb-list">
  {{ template "breadcrumb-item" (dict "step" . "start" .) }}
</ul>
{{ define "breadcrumb-item" }}
  {{ if .step.Parent }}
    {{ template "breadcrumb-item" (dict "step" .step.Parent "start" .start )  }}
  {{ else if not .step.IsHome }}
    {{ template "breadcrumb-item" (dict "step" .step.Site.Home "start" .start )  }}
  {{ end }}
  {{ $crumb := .step.Title }}
  {{ with .step.Params.crumb }} {{ $crumb = . }} {{ end }}
  <li> <a {{ with .step.IsHome }}rel="me" {{ end }}href="{{ .step.Permalink }}">{{ $crumb }}</a> </li>
{{ end }}
{{< /code >}}

[IndieWeb]: /tags/indieweb

* The `crumb` versus `Title` distinction produces a short breadcrumb trail with useful titles for each step.
* Since I removed my link to home, I need that first breadcrumb link to have a `rel="me"` attribute for
  [IndieWeb][] functionality.

## The breadcrumb index files

I need `_index` files for the intermediate steps. This breadcrumb will only list steps that have some kind of
content attached. Anything else gets skipped, which makes sense but the result's a bit confusing for me.

![Random Geekery -> Posts -> Hugo Breadcrumbs](skipped-steps.png
  "Even though the path is `posts/2020/06/hugo-breadcrumbs`!")

Can't have that.
Let's generate `_index.md` for the intermediate folders.

{{< aside >}}
[Python]: /tags/python

What say we skip the [Python][] code for generating the `_index` files.
It adds bulk to this post and is mainly relevant to 20 year old sites with a lot of cruft.
I can share it later if anyone's *that* interested.
{{< /aside >}}

Well that was fun!
Now I have a bunch of files with `crumb` and `title` front matter appropriate to their location.

{{< code file="content/post/2020/06/_index.md" >}}
---
crumb: '06'
title: June 2020 Posts
---
{{< /code >}}

{{< aside >}}
Took me a couple tries to get this just so.
Had to lean on our good friend `find` to clean up after myself along the way.

{{< console >}}
$ find ./content/{note,post} -name '_index.md' -delete
{{< /console >}}
{{</aside >}}

### Make sure next/prev work

#### For single pages

{{< code file="layouts/partials/timeline.html" >}}
{{ $typePages := where .Site.RegularPages "Type" .Type }}
<nav class="content-timeline">
  <section class="content-timeline-prev">
    <header>
      <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
      Previous {{ .Type | title }}
    </header>
    {{ with $typePages.Prev . }}
      <p>
        <a href="{{ .RelPermalink }}">{{ .Title }}</a>
      </p>
      <footer>{{ .Date.Format $.Site.Params.DateForm }}</footer>
    {{ else }}
    <p><em>You are reading the oldest {{ .Type }}</em></p>
    {{ end }}
  </section>
  <section class="content-timeline-next">
    <header>
      Next {{ .Type | title }}
      <i class="fa fa-chevron-circle-right" aria-hidden="true"></i>
    </header>
    {{ with $typePages.Next . }}
      <p>
        <a href="{{ .RelPermalink }}">{{ .Title }}</a>
      </p>
      <footer>{{ .Date.Format $.Site.Params.DateForm }}</footer>
    {{ else }}
      <p><em>You are reading the newest {{ .Type }}</em></p>
    {{ end }}
  </section>
</nav>
{{< /code >}}

## This also fixes my archives

This is kind of a double win.

For a while I was using =year= front matter. That worked, but it was extra noise in the front matter for /every/ dated entry.

So I looked around and switch to a variation of the =archm= / =archy= approach.

# Is there an easier way?

Probably, but this is much clearer than either of the solutions I used before.