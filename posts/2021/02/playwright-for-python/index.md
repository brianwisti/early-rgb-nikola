---
title: Playwright for Python
cite:
  url: https://playwright.dev/python/
  site: https://playwright.dev
  name: Playwright for Python
  description: Cross-browser end-to-end testing for modern web apps
date: 2021-02-28
slug: playwright-dev
tags:
- python
- testing
- browser testing
category: bookmark
type: micro
---
[Playwright]: https://playwright.dev/python/

A Python interface to the very handy [Playwright][] browser automation library.
The 1.9.x releases feel more Pythonic.
Naming conventions, stuff like that.
Feels much less like just a wrapper.

Don't forget to install browser drivers whenever you install or upgrade Playwright!

```console
$ python -m playwright install
```

## With pytest

[pytest-playwright]: https://github.com/microsoft/playwright-pytest
[pytest-django]: https://pytest-django.readthedocs.io/en/latest/index.html

The [pytest-playwright][] plugin provides fixtures, marks, and extra `pytest` args for browser testing.
So far the only fixture I've used is `page`, the standin for a default browser session.
Pairs nicely with [pytest-django][]'s `live_server` fixture.

Headless by default, but use `pytest --headful` if you want to watch the browser do its thing.

{{< note >}}

Since pytest-playwright is still in *early* days --
0.0.12 as of this bookmark date --
dependency managers might not acknowledge new releases.
Watch the repo and manually update your dependencies when you see a new release.

{{< /note >}}