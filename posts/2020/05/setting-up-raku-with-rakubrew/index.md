---
title: Setting up Raku with Rakubrew
slug: setting-up-raku-with-rakubrew
aliases:
- /post/2020/05/setting-up-raku-with-rakudobrew/
description: Rakudobrew changed its name since last I looked
draft: false
date: 2020-05-19 16:38:00-07:00
tags:
- rakulang
- version manager
- tools
---
I was avoiding Rakudobrew for some now-forgotten technical reason.
Probably couldn’t get a particular Perl 6 release to build. But I’m
tired of one-off scripts or distribution packages that don’t quite match
my expectations. What’s new in the Perl 6 language manager world?

For starters, names have changed. Perl 6 has been
[Raku](https://raku.org/) for a little bit, and Rakudobrew is now
[Rakubrew](https://rakubrew.org/).

I don’t recall enough about Rakudobrew to make a better or worse
comparison. Let’s just install it and see how it works.

Unfortunately `curl` doesn’t like the rakubrew site.

``` console
$ curl https://rakubrew.org/install-on-perl.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (60) SSL certificate problem: certificate has expired
More details here: https://curl.haxx.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
```

Firefox thinks the site’s fine, though. I’ll download
`install-on-perl.sh` and run it locally. Oh nice, shell initialization
instructions specific to the shell I’m running.

``` console
$ sh ~/Downloads/install-on-perl.sh
Downloading rakubrew...
Installing rakubrew to /home/random/.rakubrew ...

Load rakubrew automatically in `zsh` by adding

  eval "$(/home/random/.rakubrew/bin/rakubrew init Zsh)"

to ~/.zshrc.
This can be easily done using:

  echo 'eval "$(/home/random/.rakubrew/bin/rakubrew init Zsh)"' >> ~/.zshrc
```

I do not yet have rakubrew on all my machines, but I *do* have nearly
the same config everywhere thanks to an [Org config](/tags/orgconfig)
file. The logic I want looks a little more like this.

{{< code file="~/.zshenv" lang="zsh" >}}
export RAKUBREW_HOME="$HOME/.rakubrew"

if [ -d "$RAKUBREW_HOME" ]; then
    eval "$($RAKUBREW_HOME/bin/rakubrew init Zsh)"
fi
{{< /code >}}

Time to reload my shell and see if it worked.

``` console
$ rakubrew --help
Usage:
     rakubrew version          # or rakubrew current
     rakubrew versions         # or rakubrew list
     rakubrew global [version] # or rakubrew switch [<version>]
     rakubrew shell [--unset|<version>]
     rakubrew local [<version>]
     rakubrew nuke [<version>] # or rakubrew unregister [<version>]
     rakubrew rehash

     rakubrew available        # or rakubrew list-available
     rakubrew build [<backend>] [<tag>|<branch>|<sha-1>] [--configure-opts=<options>]
     rakubrew triple [<rakudo-version> [<nqp-version> [<moar-version>]]]
     rakubrew register <name> <path>
     rakubrew build-zef
     rakubrew download [<backend>] [<rakudo-version>]

     rakubrew exec <executable> [<executable-args>]
     rakubrew which <executable>
     rakubrew whence [--path] <executable>
     rakubrew mode [env|shim]
     rakubrew self-upgrade
     rakubrew init

     rakubrew test [<version>|all]

     rakubrew help [--verbose|<command>]
     rakubrew home
     rakubrew rakubrew-version
```

Apparently\! Can I install a fresh version of
[Rakudo](https://rakudo.org)?

``` console
$ rakubrew download
Downloading https://rakudo.org/dl/rakudo/rakudo-moar-2020.05.1-01-linux-x86_64.tar.gz
Extracting
Done, moar-2020.05.1 installed
```

Yes indeed. Pretty quick, too. Looks like I no longer need to do a full
build every time there’s a release. Nice.

Now make `moar-2020.05.01` the default.

``` console
$ rakubrew switch moar-2020.05.1
Switching to moar-2020.05.1
```

And what can Raku tell me about itself? I’ll recycle my one-liner from
[a little bit ago](/post/2019/11/building-rakudo-and-moarvm-on-linux/).

``` console
$ raku -e 'say "Yo, World! This is $*PERL - specifically: { ($*PERL, $*VM, $*DISTRO).map({ $_.gist })}"'
Yo, World! This is Raku - specifically: Raku (6.d) moar (2020.05) manjaro (3.10.0.514.10.2.el.7.x.86._.64)
```

Now the real test. Can I install
[perl6-readline](https://github.com/drforr/perl6-readline) via
[zef](https://github.com/ugexe/zef) for the Raku REPL?

``` console
$ zef install Readline
===> Searching for: Readline
===> Updating cpan mirror: https://raw.githubusercontent.com/ugexe/Perl6-ecosystems/master/cpan1.json
===> Updating p6c mirror: https://raw.githubusercontent.com/ugexe/Perl6-ecosystems/master/p6c1.json
===> Updated p6c mirror: https://raw.githubusercontent.com/ugexe/Perl6-ecosystems/master/p6c1.json
===> Updated cpan mirror: https://raw.githubusercontent.com/ugexe/Perl6-ecosystems/master/cpan1.json
===> Searching for missing dependencies: LibraryCheck
===> Testing: LibraryCheck:ver<0.0.9>:auth<github:jonathanstowe>:api<1.0>
===> Testing [OK] for LibraryCheck:ver<0.0.9>:auth<github:jonathanstowe>:api<1.0>
===> Testing: Readline:ver<0.1.5>:auth<github:drforr>
[Readline]
===> Testing [OK] for Readline:ver<0.1.5>:auth<github:drforr>
===> Installing: LibraryCheck:ver<0.0.9>:auth<github:jonathanstowe>:api<1.0>
===> Installing: Readline:ver<0.1.5>:auth<github:drforr>
```

Aw man.
[drforr](https://news.perlfoundation.org/post/remembering-jeff-goff)
sure has cast a long shadow. We’ll be missing him for a while.

And with that, I think I’ll sign off on this post. Everything I needed
installed cleanly, including [p6doc](https://github.com/Raku/doc) and a
few other [modules](https://modules.raku.org) for puttering with the
site. Rakubrew worked\!