---
title: Added dark mode for the site
slug: added-dark-mode-for-the-site
date: 2020-02-02 19:45:13-08:00
tags:
- site
- css
uuid: d2c9f3f3-8e9a-4ecb-b2c8-a264474713e9
aliases:
- /note/2020/33/added-dark-mode-for-the-site/
category: note
type: micro
previewimage: /images/2020/02/added-dark-mode-for-the-site/cover.png
---
Got tired of blowing my eyeballs out during evening work.

How? I used
[prefers-color-scheme](https://developer.mozilla.org/en-US/search?q=prefers-color-scheme).
It tries to respect existing light/dark mode settings. Here’s the
stylesheet short version.

``` scss
:root {
  --text-color:                 hsl(0, 0%, 0%);
  --content-background-color:   hsla(0, 0%, 100%, 0.8);
}

@media (prefers-color-scheme: dark) {
  :root {
    --text-color:               hsl(0, 0%, 100%);
    --content-background-color: hsla(0, 0%, 0%, 0.8);
  }
}

#page-content {
   background-color: var(--content-background-color)
   color:            var(--text-color);
}
```