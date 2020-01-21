---
title: Taskwarrior Sync
year: '2020'
draft: true
tags:
- taskwarrior
series:
- Taskwarrior Babysteps
category: tools
---
tl;dr
.. TEASER_END

What?
=====

.. note::

  None of these solutions are permanent.
  I have tried all of these.
  By carefully following directions, my task history came along intact.
  As long as your local machine is freshly synchronized, you lose nothing!

Shared folders
==============

Easy up front, but more work down the line.
Just put your taskwarrior data files in ``~/Dropbox`` or ``~/Sync`` or wherever.
Need to be careful about version drift.

Hosted task servers
===================

They do the most fiddly parts of setup.
You get instructions on what you need to do.
Pretty much just save your keys.
Easy to reach anywhere you have Internet access.

OTOH you don't know much about who's running it.
Is this a hobby? 

inthe.AM
--------

* `inthe.AM`_
* A decent Web interface, which I almost never use.
* Trello integration, which I *really* never use.
* Found the instructions easy to follow.

.. _inthe.AM: https://inthe.AM

.. note:: inthe.AM has an expired cert as of 2020-01-20, check back on this before posting.

Freecinc
--------

.. _Freecinc: https://freecinc.com/
.. _freecinc-web: https://github.com/freecinc/freecinc-web

* No frills — but maybe that's a good thing, since I never use inthe.AM's frills.
* MIT License. Clone `freecinc-web`_ and deploy your own instance!
  Admittedly that's a bit more fiddly.


Running your own taskd
======================

Nits and Caveats
================

* Cutting down on the verbosity
