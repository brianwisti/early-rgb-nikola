---
draft: true
title: Rebuilding my site database
tags:
- IndieWeb
- JuliaLang
- Data
- Site
- programming
series:
- fixing my webmentions
date: 2021-05-17
---
One thing that tripped up my Webmention flow was the fact that folks have mentioned my front page and some of my tags.
My webmention code so far references a version of [`site.db`](/post/2020/05/querying-hugo-content-with-python/) which is based on the output of `hugo list all`.
But that command only lists regular content: posts, notes, pages, bookmarks, stuff like that.
No tags, no sections, no front page.

Plus, my front matter has changed a bit.
Announcements are in a `social.json` file instead of the page frontmatter.

Everything's broken.
So it's time to revisit the site database, by looking at files in `content/` rather than expecting `hugo` to do all the work.

## Walking `content/`

```julia
pwd()
```

```
"/home/random/Sites/rgb-hugo-legacy/content/draft/rebuilding-my-site-databa
se"
```





## Loading frontmatter


## Loading announcements


## What's next?

I have a database of site content.
I have a JSON feed describing reactions to that site content.
Next time, I get to insert that JSON feed into the site database.