---
aliases:
- /post/2017/elscreen/
date: 2017-01-11T00:00:00Z
draft: false
tags:
- emacs
- elscreen
title: elscreen
year: '2017'
category: tools
---
I use [ElScreen] every time I open Emacs. May as well make a quick note about it.

[ElScreen]: https://github.com/knu/elscreen/
<!-- TEASER_END -->

I admit it. I'm still more of a [Vim][] user. The workflow I'm used to is Vim with some tabs, usually sitting
in a [tmux][] session. When in Emacs I use [ElScreen][], which basically gives me tmux inside Emacs.

If you know what that means, great. If not, then pretend ElScreen is a weird way to make emacs a tabbed editor.

[Vim]: http://www.vim.org/
[tmux]: https://tmux.github.io/

## Install It

[ErgoEmacs][] has a nice [guide to using the Emacs package manager][]. With that as your guide, find and
install the [elscreen package][] from [MELPA][].

[ErgoEmacs]: http://ergoemacs.org/
[guide to using the Emacs package manager]: http://ergoemacs.org/emacs/emacs_package_system.html
[elscreen package]: https://melpa.org/#/elscreen
[MELPA]: https://melpa.org/

Start ElScreen in your init file.

```elisp
(elscreen-start)
```

Now the elscreen commands are available throughout your Emacs session.

## Use It

[ElScreen Usage][] shows *many* commands for ElScreen. I manage with just a few.

[ElScreen Usage]: https://github.com/knu/elscreen#usage

Function            | Keys    | Description
--------------------|---------|-------------------------------------
`elscreen-create`   | `C-z c` | Create a new screen and switch to it.
`elscreen-next`     | `C-z n` | Cycle to the next screen
`elscreen-previous` | `C-z p` | Cycle to the previous screen
`elscreen-kill`     | `C-z k` | Kill the current screen
`elscreen-help`     | `C-z ?` | Show ElScreen key bindings

I know. A tutorial or something would be nice. But every time I start to write a tutorial for something, I
think of one more detail that hasn't been covered and the cycle starts all over again on the new detail. Just
needed *something* here so I could shut my brain up about "why don't you mention ElScreen?"
