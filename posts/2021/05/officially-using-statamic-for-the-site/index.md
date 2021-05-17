---
title: Officially Using Statamic For The Site
date: 2021-05-07
description: Hugo's fine but I needed to try something new
cover_image: covers/2021.officially-using-statamic.png
tags:
- site
- statamic
- cause it's there
- my brand
- Oooh a sparkly
previewimage: /images/2021/05/officially-using-statamic-for-the-site/cover.png
---
[Webmention]: https://webmention.io
[Plausible]: https://plausible.io

Got the [Webmention] pingbacks up.
Got the [Plausible] token in place.
Got server configuration and deployment working.

[Statamic]: https://statamic.com
[PHP]: https://php.net
[Laravel]: https://laravel.com/
[Laracasts]: https://laracasts.com/

Got — server configuration?
Well yeah.
The [Statamic] CMS runs on [PHP].
I *could* generate and push a static site with it, but I want to try some [Laravel] stuff.
Been watching [Laracasts] even.

## What's different?

[PaperCSS]: https://www.getpapercss.com/

The visual style, obviously.
But I cycle through those routinely.
This one's [PaperCSS] with a few tweaks.

[art]: /art
[task]: /tags/taskwarrior
[my store]: https://www.designbyhumans.com/shop/randomgeek/

I added a new section for my [art] — specifically for the art you can buy somewhere.
That's been on my [task] list for a long time.
Feels nice to get it out of the way.
I have a sizable backlog of stuff I wanted to put on [my store].
That art section will remind me to get through that backlog a bit more quickly.

You can search!
Just by title or tag for now, but I'll add more as I figure out how to fine tune it.
And because you can search, I'm not *as* worried about how pagination is handled.
I'm sure I'll add something later.

And also because you can search, I haven't gotten to the page aliases yet.
Lots of broken inbound links, I expect.
If this were some kind of professional site, I would've waited until I had those in place.
But it's not.
So I don't.

## Anything else?

From your perspective, that's about it.
It's pretty much the same site.

From my perspective, so much!
I get an awesome control panel to manage and edit content.
All my pages are still in flat text files, so I can edit them in my favorite text editor with no fuss.

Okay that's not new for the site.
It's new compared to when I tried this with WordPress though.

## What's different from stock Statamic Solo?

[SASS]: https://sass-lang.com/
[Tailwind]: https://tailwindcss.com/

The styling is set up with [SASS] instead of the starter's default of [Tailwind].
Probably shift back once I figure out an approach to content styling that I prefer to Tailwind Prose.

I don't entirely trust server-side for a blog.
Nothing to do with Statamic or PHP mind you.
It's just too easy to miss important details when you're running a solo project.

[2FA]: https://statamic.com/addons/jrc9designstudio/2fa
[Gitamic]: https://statamic.com/addons/simonhamp/gitamic

With that in mind, I added [2FA] for two factor authentication and [Gitamic] for Git integration.
Both are paid add-ons.
Much as I love open source software, I love knowing that good developers get a good dinner even more.
Sponsorship and patronage only go so far — on my monthly budget, at least.

## What's next?

There's still some basic deployment stuff to figure out.
Metadata for sharing, or what the boring kids call "SEO."
Ugh.
I ain't optimizing *nothin'*, least of all some search engine's job.

Anyways.
Then comes automating the non-RSS syndication: posting toots and tweets when I hit "Publish."
Until I get that code in it's manual, so I'll probably skip those for my notes.

After that?
Watch Laracasts.
Learn Laravel.
Learn Statamic.
Have fun.