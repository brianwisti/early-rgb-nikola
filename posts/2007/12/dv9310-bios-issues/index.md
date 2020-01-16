---
aliases:
- /blogspot/2007/12/29_now-that-both-of-my-machines-are.html
- /post/2007/now-that-both-of-my-machines-are/
categories:
- Blogspot
date: 2007-12-29T00:00:00Z
tags:
- troubleshooting
title: dv9310 bios issues
type: post
update: 2008-01-08
year: '2007'
---
<b>Update:</b> I turned my offhand comment about how I fixed my problem into more of a step-by-step guide, in case some poor soul is in the same spot and finds me via Google.
<!--more-->

Now that both of my machines are healing again - did I mention that a BIOS update flattened my HP dv9310? Oh, it flattened my HP all right. The new one effectively  makes the computer forget that it has a video card. If you do an update and the machine starts spontaneously rebooting, try this:

<ol>
<li>Boot into Safe Mode</li>
<li>Go to your Device Manager and disable the NVidia card. It's okay, you'll still have normal VGA.</li>
<li>Reboot in normal mode.</li>
<li>Go to the HP support site and download an older BIOS version.</li>
<li>Install that older BIOS.</li>
<li>Reboot.</li>
<li>Go to your Device Manager and re-enable the NVidia card.</li>
</ol>

Everything should be okay now.

Anyways, the machines are reconfigured, I've sparked my brain with a little Python code, and now I can get back to a Perl project that's been waiting over a month.
