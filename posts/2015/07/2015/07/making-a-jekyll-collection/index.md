---
aliases:
- /tools/2015/07/19_making-a-jekyll-collection.html
- /post/2015/making-a-jekyll-collection/
announcements:
  twitter: https://twitter.com/brianwisti/status/622878343470256128
date: 2015-07-19T00:00:00Z
description: I am curious about Jekyll's experimental collections feature and whether
  it could be useful for me.
tags:
- jekyll
- site
title: Making a Jekyll Collection
type: post
updated: 2015-08-07T00:00:00Z
year: '2015'
category: tools
---
[Jekyll]: http://jekyllrb.com
[collections]: http://jekyllrb.com/docs/collections/
[Jekyll][] currently generates the HTML for my site. I am curious about the
experimental [collections][] feature, and whether it could be useful for me.
<!--more-->

This post should not be too difficult to read along with - and I will happily fix
any problems you notice - but I do assume you know the basics of creating a blog
with Jekyll. The code and templates were initially build on Jekyll 3.0.0.beta8.

## Updates

### 2015-08-07

Reader Eric Tirado noticed that I broke the individual crafts project links -
again. So I fixed it for real. Just set the collection `permalink` to
something useful in `_config.yml`.

### 2015-07-21

I ended up having several issues attributable to either collections under
Jekyll 3.0 beta or Octopress 3. Decided to switch to Jekyll 2.5.3 and made
a few adjustments to the collections template. Everything *seems* okay now.

## What? Why?

So what the heck is a collection? From the Jekyll [collections][] documentation:

> Not everything is a post or a page. Maybe you want to document the various
> methods in your open source project, members of a team, or talks at a
> conference. Collections allow you to define a new type of document that behave
> like Pages or Posts do normally, but also have their own unique properties and
> namespace.

Collections could be useful when you have things you want to show
on your site without necessarily being tied to the blog-centric structure of Posts
or the simple content dump of a Page.

Who would that help, besides the slightly technical examples from the
description?

* A writer could organize their stories into collections
* An artist could present their works as one or more collections
* A knitter could put their yarn projects in a collection.
* Anyone who takes pictures could use collections as photo galleries.
* Recipes, maybe?
* Music playlists!
* All the books I own, and the few I have actually read!

A blog post probably works for most of these use cases. Maybe fiddle a bit with
categories and put a tag here and there, and your content is out there for
anyone. Good enough.

"Good enough" isn't good enough for every case, though. Occasionally you want to
tune some of your content in a special way. You may find this is easier with
collections than with blog posts.

There are also dedicated sites for all of these ideas, and those are good
enough too. Some excel at the services they provide. They have concerns too. Now
the visibility of your creations is tied to the fortunes and policies of
whoever provides that service. Keeping that in a collection on your own site
gives you a backup if the service goes away, at least.

[knitting]: /categories/knitting/
[account]: http://www.ravelry.com/people/brianwisti
[Ravelry]: https://www.ravelry.com

I could use collections for my knitting and crochet projects. I have a
couple of [knitting][] blog posts here, and an [account][] on [Ravelry][]
highlighting a handful of other WIPs[^1] and FOs[^2]. The blog posts work fine as blog
posts, but I still want a separate way to organize those projects. The stuff on
Ravelry can only be seen if you have an account with the service. That's fine,
but I have spent 2015 consolidating material I've created elsewhere onto my
site. Ravelry is a reasonable next target for me.

## Fine. How?

[configuration]: http://jekyllrb.com/docs/configuration/
First I need to add a `collections` entry to my `_config.yml` [configuration][]
file. This entry contains a list of all collections in the site, and metadata
for each collection. I want these collections displayed on the site, so I must
set the `output` metadata for the collection to `true`. I also want to be sure
individual project pages are given consistent URLs, which has been an issue for
me bouncing between Jekyll 2.5.3 and Jekyll 3.0.0 beta. Setting `permalink`
takes care of that issue.

``` yaml
collections:
  crafts:
    output: true
    permalink: /crafts/:path/
```

Next I create the folder to hold this collection. By default its name must
match the collection name with an underscore prefix.

    $ mkdir _crafts

### One Thing

[garter stitch scarf post]: /post/2015/quick-garter-scarf/
Time to put something in the collection. I can use my recent [garter stitch scarf post][] as a
starting point, filling in the details of a new collection item from that post.

    $ atom _crafts/garter-scarf-wrapped.markdown

