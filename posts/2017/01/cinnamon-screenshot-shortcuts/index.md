---
aliases:
- /post/2017/cinnamon-screenshot-shortcuts/
announcements:
  twitter: https://twitter.com/brianwisti/status/815473860254408704
date: 2017-01-01T00:00:00Z
draft: false
tags:
- linux
- cinnamon
title: Cinnamon Screenshot Shortcuts
year: '2017'
category: tools
previewimage: /images/2017/01/cinnamon-screenshot-shortcuts/cover.png
---

*TL;DR:* Cinnamon screenshot and recording shortcuts are in Settings -> Hardware -> Keyboard -> Shortcuts ->
System.
<!-- TEASER_END -->

****

I used Linux Minut 18.1 for this post. I cannot verify whether this information applies to earlier or
later versions.

****

I take many screenshots during my day, for work and for fun. I use the Cinnamon desktop environment in [Linux
Mint][]. I kept forgetting the keyboard shortcuts to do screenshots directly from the desktop rather than
opening up [GNOME Screenshot][].

[GNOME Screenshot]: https://help.gnome.org/users/gnome-help/stable/screen-shot-record.html.en
[Linux Mint]: https://linuxmint.com/

Here are the default shortcuts. You can customize them in Keyboard Settings, as shown in the image that started this post.

Action                        | Shortcut
------------------------------|--------------------------
Take a screenshot             | `Print`
Take a screenshot of a window | `Alt` + `Print`
Take a screenshot of an area  | `Shift` + `Print`
Copy area to clipboard        | `Shift` + `Control` + `Print`
Copy screen to clipboard      | `Control` + `Print`
Copy window to clipboard      | `Control` + `Alt` + `Print`
Toggle recording desktop      | `Shift` + `Control` + `Alt` + `R`

`Print` may have its own special label on your keyboard. On mine the `Print` key is labeled `PrtSc`.

Next, with pictures!

## Take A Screenshot

The `Print` key alone will save your entire screen.

{{< show-figure image="cinnamon-fullscreen-screenshot.png"
  description="Fullscreen screenshot, scaled down in GIMP" >}}

## Take A Screenshot Of A Window

`Alt` and `Print` together to save a single window.

{{< show-figure image="cinnamon-window-screenshot.png"
  description="Window screenshot, scaled down in GIMP" >}}

## Take A Screenshot Of An Area

`Shift` + `Print` for an area screenshot. Your mouse point will change to a crosshair. Click and drag to
select the area you want to save.

{{< show-figure image="cinnamon-area-screenshot.png"
  description="An area on the Linux Mint home page" >}}

Sometimes I had to hit this combo a few times to get it work. That could be a software bug somewhere or it
could just be grit in my keyboard.

## Record Desktop

****

Okay I've never done this part before. I probably missed something important. Be warned if you try it
yourself.

****

`Control` + `Shift` + `Alt` + `R` will start recording your desktop, and the same combo will end the recording
session. No sound is recorded. Recordings are saved as [WebM][] files in your home directory. [WebM support][] is
widespread, although some browsers require codecs to be installed.

[WebM]: http://www.webmproject.org/
[WebM support]: http://caniuse.com/#feat=webm


For more advanced screen recording functionality, [recordMyDesktop][] looks like a good bet.

[recordMyDesktop]: http://recordmydesktop.sourceforge.net/about.php

I tried several times before I noticed a little red light in the lower right corner when recording is
active. 

Wanted to show you a video of the area screenshot functionality. The keyboard shortcut for that doesn't seem
to work when recording. Instead I made a video of using the screenshot application.

Since this is more to show about recording videos than anything else, I decided the full resolution video was
not needed. I installed [FFmpeg][] and used it to resize the video, following this [FFmpeg resizing
tutorial][].

[FFmpeg]: http://ffmpeg.org/
[FFmpeg resizing tutorial]: https://trac.ffmpeg.org/wiki/Scaling%20(resizing)%20with%20ffmpeg

```console
$ sudo apt-get install ffmpeg
$ ffmpeg -i ~/cinnamon-20161231-9.webm -vf scale=720:-1 \
  static/video/2017/cinnamon-desktop-recording.webm
```

Ta-da!

<video src="/video/2017/cinnamon-desktop-recording.webm" controls>
</video>

Well - "ta-da" assuming your browser supports [WebM][].

