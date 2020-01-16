---
aliases:
- /tools/2015/07/16_remote-editing-in-atom.html
- /post/2015/remote-editing-in-atom/
categories:
- tools
date: 2015-07-16T00:00:00Z
description: I am slowly learning more about how to use Atom for real work.
tags:
- atom-editor
title: Remote Editing In Atom
type: post
year: '2015'
---
[Atom]: https://atom.io
[remote-atom]: https://atom.io/packages/remote-atom
I am slowly learning more about how to use [Atom][] for real work. First
requirement: my "real work" almost exclusively takes place on a virtual
machine. Atom alone cannot handle editing those files. [remote-atom][] to the
rescue!
<!--more-->

[Vim]: http://www.vim.org
Well, sort of. It's not as reflexive as bouncing around in a [Vim][] session,
but some of that must be due to lack of familiarity.

It works, though.

[Settings View]: https://atom.io/packages/settings-view
[master copy]: https://raw.githubusercontent.com/aurora/rmate/master/rmate
You can install the remote-atom package from Atom's [Settings View][].
Follow the directions on the [remote-atom][] package page,
and you'll end up with a `rmate` executable on your virtual machine,
corresponding to a [master copy][] in the remote-atom git repo.

[Command Palette]: https://atom.io/packages/command-palette
`rmate` communicates with the Remote Atom service, which you need to manage
yourself. You can do this from the _Packages_ menu, but I want to get
comfortable with the [Command Palette][].

{{< show-figure image="remote-atom-start-server.png"
  description="Start Remote Atom Server from Command Palette" >}}

Once the server is available, you can `rmate` files to your heart's content.

    $ rmate lib/secret-work-stuff
    $ rmate test/secret-work-tests

No point showing a screenshot of `lib/secret-work-stuff`, because it's just
another tab as far as the [Atom][] user interface is concerned. Saving
correctly updated the file on my virtual machine. Simple and straightforward.

Eventually you may want to stop the server. Again, from the [Command Palette][].

{{< show-figure image="remote-atom-stop-server.png"
  description="Stop Server from Command Palette" >}}

I'm still not ready to use [Atom][] as my primary or even secondary editor, but
it's starting to feel useful, thanks to packages like [remote-atom][].
