---
date: 2020-05-07 14:30:00-07:00
tags:
- emacs
- OrgConfig
title: Made an Emacs Binding for Config Quick Edit
slug: made-an-emacs-binding-for-config-quick-edit
uuid: 134490e5-3176-45cb-84f3-74db08812620
category: note
type: micro
---
I hit `F5`, Emacs opens my
[`config.org`](/post/2020/04/from-dotfiles-to-org-file) for editing. It
might not be much but it feels good to scratch such a specific itch.
Feeling pretty good about myself.

``` elisp
(global-set-key (kbd "<f5>")
                (lambda ()
                  (interactive)
                  (find-file "~/.dotfiles/config.org")))
```