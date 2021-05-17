---
title: Sending Webmentions
uuid: eba0c072-c758-4232-95cd-a02c6dd98abd
description:
caption:
tags:
- IndieWeb
- perl
- tools
draft: true
date: 2021-05-17
---
Okay. You have your
[h-card](/post/2020/04/h-entry-microformat-for-indieweb-posts/). Your
posts have [h-entry](/post/2020/04/indieweb-h-cards/index.adoc/)
details. You’re listening for responses on webmention.io. You are ready
to start talking to the IndieWeb.

## Concepts

Anybody can link to my site. I can look at an analytics dashboard or
server log to figure out where visitors come from, assuming the [HTTP
Referer
header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
was set up correctly. If someone wants me to know what they think about
a post, they can email me, tweet at me, or whatever. Maybe we keep an
eye out for each others' names in our respective RSS readers.

[Webmentions](https://webmention.net/draft/) let us actively use our Web
sites as a medium for conversation. The Webmentions draft summarizes how
this works:

{{< quote
  cite="https://webmention.net/draft/#overview"
  source="Webmention Editor's Draft: Overview" >}}
A typical Webmention flow is as follows:

1.  Alice posts some interesting content on her site (which is set up
    to receive Webmentions).

2.  Bob sees this content and comments about it on his site, linking
    back to Alice’s original post.

3.  Using Webmention, Bob’s publishing software automatically notifies
    Alice’s server that her post has been linked to by the URL of
    Bob’s post.

4.  Alice’s publishing software verifies that Bob’s post actually
    contains a mention of her post and then includes this information
    on her site.
{{< /quote >}}

Sounds fiddly. No point pretending otherwise — it can be. The tools that
enable Webmentions are mostly written by and for folks who like to
tinker. But the core ideas aren’t so bad:

1.  I post something.
2.  You post something, and tell me it’s a response to my post.

This may bring the
[Pingback](https://www.hixie.ch/specs/pingback/pingback) mechanism to
mind for bloggers of a certain age. Yes indeed\! Pingbacks inspired
Webmentions, though changes were made along the way. For example, they
switched the XML-RPC transaction out for a form-encoded `POST` over
HTTP.

[reply](https://indieweb.org/reply)
: Someone has something to say about you or your post

[like](https://indieweb.org/like)
: Someone thinks your post is awesome

[bookmark](https://indieweb.org/bookmark)
: Someone shared a link to your post, building a reading list for
  themselves or someone else

[repost](https://indieweb.org/repost)
: Someone shared your post, generally without additional comment

There are several more [responses](https://indieweb.org/responses) in
common use, and many more are possible!

## The webmention tools landscape

There are many libraries and tools for [sending
Webmentions](https://indieweb.org/Webmention-developer#Sending). Most
provide varying degrees of functionality and documentation. Try the ones
available for your favorite language. And if that’s not close enough to
the metal for you? Use [curl](https://curl.haxx.se/) or
[HTTPie](https://httpie.org/) and [send your mentions
yourself](https://aaronparecki.com/2018/06/30/11/your-first-webmention).

Good luck!

I ended up going with {{< card-link "Jason McIntosh" >}}'s
[Web::Mention](https://metacpan.org/pod/Web::Mention), written in Perl.
The examples showed how to use it, and how to get at errors when needed.

This is gonna play hell with my Year of Python.

I made a little [test
note](/note/2020/05/pondering-my-indieweb-guinea-pig/) with an h-card
link. The convention for [person-tags](https://indieweb.org/person-tag)
is to add `u-category` to the link classes. Learned something new\!

``` html
…<a class="u-category h-card" href="http://jmac.org/">Jason McIntosh</a> seems like a
reasonable choice to test Webmentions on…
```

I wrote a script with hard-coded values for source and target.

{{< code file="send-mention.pl" >}}
use Web::Mention;

use 5.30.0;
use warnings;

my $source = "https://randomgeekery.org/note/2020/05/pondering-my-indieweb-guinea-pig/";
my $target = "http://jmac.org";

my $wm = Web::Mention->new(
  source => $source,
  target => $target,
);
my $success = $wm->send;

if ( $success ) {
  say "Webmention sent successfully";
} else {
  say "Unsuccessful!";
  say $wm->response->as_string;
}
{{< /code >}}

I published the note: build, push, and announce to my main social
networks.

{{< console >}}
$ invoke publish
{{< /console >}}

Full of fear and trepidation, I ran my mention script.

{{< console >}}
$ perl send-mention.pl
Webmention sent successfully!
{{< /console >}}

So. I think that worked?