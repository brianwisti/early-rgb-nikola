---
aliases:
- /post/2016/dancer2-hello/
announcements:
  twitter: https://twitter.com/brianwisti/status/752670315885441024
date: 2016-07-11T00:00:00Z
description: Some simple first steps with the Perl 5 Dancer2 web framework
draft: false
tags:
- perl
- dancer
- learn
title: Hello Dancer2
year: '2016'
category: programming
---

[Dancer2]: https://metacpan.org/pod/Dancer2
[PerlDancer]: https://github.com/PerlDancer/
[boilerplate code]: https://en.wikipedia.org/wiki/Boilerplate_code
The [PerlDancer][] team's [Dancer2][] project is a Perl framework for writing Web applications with less [boilerplate code][]
than other Web frameworks. I am slowly exploring what it offers. Feel free to follow along.
<!-- TEASER_END -->

This is sort of a tutorial. I assume you know Perl and maybe a bit about Web server programming, but not that
you have mastered either. My pace may annoy you if you *have* mastered Perl, Web programming, or
Dancer2.

### Installation

[Perlbrew]: http://perlbrew.pl/
[cpanm]: https://metacpan.org/pod/App::cpanminus

I use Perl 5.24.0 and [cpanm][] via [Perlbrew][]. Installation of Dancer2 and its dependencies requires a
single command.

    $ cpanm Dancer2

## Hey

You do not need much code to create a Dancer2 application.

```perl
use Dancer2;     # Load Dancer2 and its keywords

get '/hey' => sub { # Define some routes
  return 'Hey!';
};

start;           # Run the application
```

Even better: you can hand this code to Perl and it starts a server!

    $ perl hey.pl
    >> Dancer2 v0.200002 server 15388 listening on http://0.0.0.0:3000

Loading http://localhost:3000/hey in a browser shows our simple message.

{{< show-figure image="dancer2-hey.png"
  description="'Hey!' in Dancer2" >}}

[DSL]: https://en.wikipedia.org/wiki/Domain-specific_language
[keywords]: https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#DSL-KEYWORDS

Dancer2 gives you a [DSL][] - Domain-Specific Language - to describe your application. These
DSL [keywords][] cut down the boilerplate code common in some Web development frameworks.

[`start`]: https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#start
[`get`]: https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#get

### `get`

[route]: https://metacpan.org/pod/Dancer2::Core::Route
[HTTP]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

The [`get`][] keyword defines a [route][] for Dancer2. Routes tell Dancer2 how to respond
when someone requests a path - the `/hey` bit - from your application. The `get` keyword
is also a method from [HTTP][]. Use it when you only want to "get" something from the
application. Dancer2 has keywords for more HTTP methods, but `get` is fine for now.

****

#### What happens if someone requests a path that you did not define?

Your Dancer2 application returns an error page informing them that the path does not exist.

****

With the HTTP method and path defined, the last important part of our route is the code.
Your application runs that code and sends its return value to the visitor. Our first
route code example is an anonymous subroutine that returns the text "Hello!", but they
can be as complicated as you need.

### `start`

This keyword tells Dancer2 that you finished defining your application and it can begin
serving to the world.

****

### DSL = Keywords + Sugar

Keywords make the Dancer2 DSL work, but the code style takes advantage of
Perl's flexible syntax. Our route looks like this with less [syntactic sugar][].


```perl
get('/hey', sub { return 'Hey!'; });
```

****

[syntactic sugar]: https://en.wikipedia.org/wiki/Syntactic_sugar

## Hey You

How about greeting the visitor by name? Since form processing involves more
steps than I want to think about today, we use route parameters instead.

Dancer2 allows placeholders in route paths. The simplest placeholders are tokens prefixed
with a colon, such as `:name` or `:id`. When you make a request that matches, such as
`/hey/brian`, Dancer2 saves the matching path part. Here, look at some code.

```perl
use Dancer2;

# A simple greeting: /hey
get '/hey' => sub {
  return 'Hey!';
  };
  
# A personalized greeting: /hey/Brian
get '/hey/:name' => sub {
  my $name = route_parameters->get('name');
  return "Hey $name!";
};

start;
```

[much more complicated]: https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#Route-Handlers
Route handlers can get [much more complicated][], but not today. Our application treats a general
greeting and a greeting with a distinct name at two different actions, so we use two different routes.

In order to use the new code, we need to stop the Perl process. `Control-C` should do it. Then launch it
again, and the new code will be loaded.

    $ perl hey.pl
    >> Dancer2 v0.200002 server 31385 listening on http://0.0.0.0:3000

Now we should be able to see http://localhost:3000/hey/Brian - or whatever name you prefer.

{{< show-figure image="dancer2-hey-brian.png"
  description="'Hey Brian!' in Dancer2" >}}

### `route_parameters`

[`route_parameters`]: https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#route_parameters
[hash-like object]: https://metacpan.org/pod/Hash::MultiValue

The `route_parameters` keyword returns a [hash-like object][] which stores
tokens and their values from a route match. Use the `get` method when you
need those values in your route code.

## Wrap It Up

We installed Dancer2, made just about the simplest Web application I could think
of, and explored a little bit about declaring routes.

What's next? I plan to look at using template files to produce real Web pages.

