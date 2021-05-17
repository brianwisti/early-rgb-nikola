---
title: asdf -- An extendable version manager
cite:
  url: https://asdf-vm.com/#/
  site: https://asdf-vm.com
  name: asdf - An extendable version manager
  description: An extendable version manager
date: 2021-03-23
slug: asdf-vm-com
tags:
- tools
- shell
- version manager
- crystal
category: bookmark
type: micro
---
Installed mainly because `brew install|upgrade crystal` keeps having intermittent issues for me.

``` console
$ asdf plugin-add crystal https://github.com/asdf-community/asdf-crystal.git
$ asdf install crystal 1.0.0
Crystal 1.0.0 [dd40a2442] (2021-03-22)

LLVM: 10.0.0
Default target: x86_64-unknown-linux-gnu
```

All better.