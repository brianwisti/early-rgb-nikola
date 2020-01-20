---
aliases:
- /blogspot/2007/11/26_xcbxlibunlock-issues-java-on-fedora.html
- /post/2007/xcbxlibunlock-issues-java-on-fedora/
date: 2007-11-26T00:00:00Z
tags:
- linux
- java
title: xcb_xlib_unlock issues - Java on Fedora
type: post
year: '2007'
archived_category: blogspot
---
I decided to install the Sun JDK on my new Fedora install today. Tried downloading the JDK/NetBeans self-installing bundle. It didn't work. I got an error in xcb_xlib:xcb_xlib_unlock - something about a failed assertion. While running the installer. Drat.
<!-- TEASER_END -->

Installation required skipping the Netbeans IDE and just using the self-extracting JDK archive. Then, in order to get Swing to work, I had to remove Xinerama references from any copy of libmawt.so that was in my Java install. There's a sed script floating out there, but that wasn't working for me. Before I spent effort figuring out sed, I edited the files from vim.


<pre>[brian@localhost ~]$ sudo vim /opt/jdk1.6.0_03/jre/lib/i386/xawt/libmawt.so
[brian@localhost ~]$ sudo vim /opt/jdk1.6.0_03/jre/lib/i386/motif21/libmawt.so
[brian@localhost ~]$ sudo vim /opt/jdk1.6.0_03/jre/lib/i386/headless/libmawt.so
[brian@localhost ~]$</pre>

In each case I executed a simple regex

<pre>:%s/XINERAMA/FAKEEXT/g</pre>

It's the same as the sed script. I was too lazy to fix a short script that I will probably only use once.

Java's happy now, so I'm going to go do a little coding.
