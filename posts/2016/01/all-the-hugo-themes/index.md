---
aliases:
- /post/2016/all-the-hugo-themes/
announcements:
  twitter: https://twitter.com/brianwisti/status/683446375275560960
date: 2016-01-02T00:00:00Z
description: Using Python to preview my Hugo site with many themes
image: /img/2016/chrome-redlounge-medium.png
tags:
- hugo
- python
thumbnail: /img/2016/chrome-redlounge-medium-thumbnail.png
title: All The Hugo Themes
updated: 2016-01-04T00:00:00Z
year: '2016'
category: programming
---
[Hugo]: http://gohugo.io/
[themes repository]: http://themes.gohugo.io/
[Python]: https://python.org/
My site does well enough with [Hugo][] and a custom theme, but I wanted to
explore the [themes repository][]. So I wrote some [Python][].
<!--more-->

<aside>
<h4>2016-01-04 Update</h4>

<p>Added instructions for installing dependencies with Homebrew, and clarified
some content based on comments from the <a href="https://discuss.gohugo.io">Hugo community</a>.</p>

<h4>2016-01-03 Update</h4>

<p>My checkout of the themes repository was out of date. I refreshed it this
morning, resulting in <a
href="/img/2016/hugo-themes.gif" target="_blank">a new GIF</a>.</p>
</aside>

[Hugo Quickstart]: https://gohugo.io/overview/quickstart/
[hugoThemes]: https://github.com/spf13/hugoThemes/

If you followed the [Hugo Quickstart][] then you probably already have your
own copy of the themes to use. Otherwise you might want to clone the [hugoThemes][]
repo with git.

    $ cd mysite/
    $ git clone --depth 1 --recursive https://github.com/spf13/hugoThemes.git themes


## Code

[Python]: https://python.org/
[Splinter]: https://splinter.readthedocs.org/en/latest/
[Chrome WebDriver]: https://splinter.readthedocs.org/en/latest/drivers/chrome.html
[subprocess]: https://docs.python.org/3.5/library/subprocess.html
[ImageMagick]: http://imagemagick.org/script/index.php
[convert]: http://imagemagick.org/script/convert.php

The idea here is to ask Hugo to build and serve the site once for each theme.
For each built theme, ask the browser to load and screenshot the site with that
theme.

I chose Python for this task. No special reason. I was just in a Python mood that
day.

[Splinter][] provided the browser controlling API. Since I'm using Chrome for this,
I installed the [Chrome WebDriver][]. The [subprocess][] standard
library module allowed me to control `hugo`, restarting with a fresh theme once
the browser had enough time to grab a screenshot.

Then I had a last minute idea: use the [convert][] utility from [ImageMagick][]
to collect all the screenshots into an animated GIF.

[Homebrew]: https://brew.sh

You may need to install dependencies. Everything you need *should* be available
for your platform, but I still need to double check that. Here are the steps I
followed to get things working with [Homebrew][] on my Mac.

    $ brew install python3 imagemagick chromedriver
    $ pip3 install splinter

All right - that's out of the way. Now for some code.

``` python
#!/usr/bin/env python3

import os
import os.path
import shutil
import subprocess
import time

from splinter import Browser

def is_theme_dir(folder, item):
    if item[0] == '.':
        return False
    full_path = os.path.join(folder, item)
    if os.path.isfile(full_path):
        return False

    return True

if __name__ == '__main__':
    theme_dir = "themes"
    screenshot_dir = "screenshots"
    url = "http://127.0.0.1:1313"

    # Clean up old screenshots
    for f in os.listdir(screenshot_dir):
        filepath = os.path.join(screenshot_dir, f)
        try:
            if os.path.isfile(filepath):
                os.unlink(filepath)
        except Exception as e:
            print(filepath, e)

    listing = [ item for item in os.listdir(theme_dir)
            if is_theme_dir(theme_dir, item) ]
    browser_name = 'chrome'
    browser = Browser(browser_name)
    browser.visit(url) # visit out here, reload down there because browser cache

    for theme in listing:
        command = [ "/usr/local/bin/hugo", "server", "--theme", theme ]
        hugo = subprocess.Popen(command)
        time.sleep(1) # More than enough time for Hugo to build the site.
        browser.reload()
        time.sleep(2) # Allow browser to get external resources.
        message = "Theme: {}, Status: {}".format(theme, browser.status_code)
        print(message)
        screenshot_name = "{}-{}.".format(browser_name, theme)
        screenshot_file = os.path.join(os.getcwd(), screenshot_dir, screenshot_name)
        browser.screenshot(screenshot_file)
        print("Screenshot saved as: {}".format(screenshot_file))
        hugo.kill()
    browser.quit()

    # Make an animated GIF of the whole thing.
    convert_command = [ "/usr/local/bin/convert",
            "-delay",  '50',
            "-loop",    '0',
            "-scale", '50%',
            "screenshots/*.png",
            "hugo-themes.gif" ]
    subprocess.run(convert_command)
```

## The Result

Aside from a few dozen PNG files? Well, there's that nifty animation. Animated
GIFs give me a headache sometimes, so I will <a
href="/img/2016/hugo-themes.gif" target="_blank">link to the GIF</a> instead.

## Observations

I noticed a few things with this experiment.

### Configuration

{{< show-figure image="chrome-redlounge-medium.png"
  description="Red Lounge"
  link="https://themes.gohugo.io/redlounge/"
  link-text="Theme home" >}}

Themes vary significantly in their expected configuration options. Some want
social media links under `author`. Others wanted them in `Params`.
`gravatarHash` and `GravatarHash` are two distinct options. Many have hard-coded
assumptions in their layouts: an image file `/img/avatar.jpg`, for example.
Sometimes it's called `/media/me.jpg` though.

This is not an issue if you pick a favorite from the [themes repository][] and
make your site work with your favorite. It *is* an issue if you're looking at
your site in every theme. I turned my `config.yaml` into sort of a mess to make
it work with more of the themes.

### Layout

Although many themes focus on blog content, some have a different purpose.
Their authors may have created them with project documentation, portfolios, or
company sites in mind. Their structure is more complex or requires metadata beyond
a simple blog.

I like this variety. I find that it's much easier to create sites with different
purposes using Hugo than when using Jekyll.

{{< show-figure image="chrome-artists-medium.png"
  description="Artists Theme"
  link="https://themes.gohugo.io/artists/"
  link-text="Theme home" >}}

But it does help understand why sometimes the site renders as an attractive
blank space in my preview. Examining the theme README would be a good next
step if a particular theme interested me.

Well - reading documentation for the thing you're using is generally a good idea
anyways.

### Sections

{{< show-figure image="chrome-pixyll-medium.png"
  description="Pixyll"
  link="https://themes.gohugo.io/pixyll/"
  link-text="Theme home" >}}

[craft]: /craft/
[customize your template]: http://gohugo.io/themes/customizing/
The themes seemed a little confused by my [craft][] section.
Some ignored craft projects completely, while others integrated them with posts on the
`index.html` listing. Most at least provided a menu link to the section. And yes,
the theme README would likely remove my confusion.

You will probably need to [customize your template][] if you have special
content.

## What Theme Should I Use?

[Hyde-X]: http://themes.gohugo.io/hyde-x/

Maybe you were wondering which theme you could use for your new site. I suggest
[Hyde-X][] for blog sites. It has nice defaults, and provides quality
documentation for its many configuration options. My site started with
Hyde-X as a base before moving in its own direction.

{{< show-figure image="chrome-hyde-x-medium.png"
  description="Hyde-X"
  link="https://themes.gohugo.io/hyde-x/"
  link-text="Theme home" >}}

Hyde-X isn't the only way to start. There are numerous excellent blog-focused
themes in the repository.

<aside>
I do plan on tidying up my own site theme and making it available for the
repository at some point. But - you know - I get busy sometimes.
</aside>

For non-blog sites? I don't know, to be honest. None of my content worked well
with those. Good luck with your search!

Anyways, the important thing is to have fun.
