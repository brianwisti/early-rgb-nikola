---
aliases:
- /tools/2015/07/27_itunes-to-rhythmbox.html
- /post/2015/itunes-to-rhythmbox/
date: 2015-07-27T00:00:00Z
description: I nearly wrote a script that transfers my iTunes ratings to Rhythmbox.
  Instead I used Edgar Salgado's version of iTunesToRhythm.
tags:
- itunes
- ruby
- music
title: iTunes to Rhythmbox
type: post
year: '2015'
category: tools
---
[iTunes ratings]: /post/2015/ruby-itunes-ratings-fun/
[Rhythmbox]: https://wiki.gnome.org/Apps/Rhythmbox
[iTunesToRhythm]: https://github.com/esalgado/iTunesToRhythm
I nearly wrote a script that transfers my [iTunes ratings][] to [Rhythmbox][]. Instead I used Edgar Salgado's
version of [iTunesToRhythm][].
<!--more-->

[GNOME 3]: https://www.gnome.org/gnome-3/
[openSUSE]: https://www.opensuse.org
See, I have been spending most of my time lately in [GNOME 3][] on [openSUSE][] Linux. All of my music is
copied over and loaded into [Rhythmbox][], but I wanted to continue my quest to rate all of my music. I spent
roughly an hour starting my own solution before realizing that this was probably a solved problem.

[another project]: https://github.com/esanbock/ITunesToRhythm
Salgado's code is a fork of [another project][], but he won my heart because he wrote how to use his version.

    $ git clone git@github.com:esalgado/iTunesToRhythm.git
    $ cd iTunesToRhythm
    $ python iTunesToRhythm.py -w ~/Sync/iTunes\ Music\ Library.xml ~/.local/share/rhythmbox/rhythmdb.xml

Some things about the process annoyed me. For some strange reason, not every iTunes entry included a file
location. I manually fixed those. More annoying: the iTunes XML showed roughly 7,000 tracks as rated even
though the iTunes application showed over 10,000 as rated. I chose to live with that. It's only 3,000 tracks
that I need to rate again.

*sigh*

Hey, let's make a pretty picture.

``` ruby
#!/usr/bin/env ruby

require 'nokogiri'
require 'gruff'

SOURCE = "/home/brian/.local/share/rhythmbox/rhythmdb.xml"

rhythmdb = Nokogiri::XML File.open SOURCE
songs = rhythmdb.xpath "/rhythmdb/entry[@type='song']"
ratings = {}

# Group the songs by rating.
songs.each do |song|
  rating = song.xpath("rating").text.to_i || 0
  total_time = song.xpath("duration").text.to_i || 0
  ratings[rating] ||= { songs: 0, time: 0 }
  ratings[rating][:songs] += 1
  ratings[rating][:time] += total_time
end

# Print it.
puts 'Rating Songs Percent Duration'

ratings.keys.sort.each do |rating|
  song_count = ratings[rating][:songs]
  total_seconds = ratings[rating][:time] #Rhythmbox uses seconds
  seconds = total_seconds % 60
  minutes = (total_seconds / 60) % 60
  hours = (total_seconds / (60 * 60)) % 24
  days = total_seconds / (60 * 60 * 24)

  percentage = song_count.to_f() / songs.count.to_f() * 100.0
  duration = format '%02d:%02d:%02d:%02d', days, hours, minutes, seconds
  description = format '%6d %5d %6.1f%% %s', rating, song_count, percentage, duration
  puts description

# Graph it.
data = ratings.map { |rating, info| [ rating, [ info[:songs]]] }

graph = Gruff::Pie.new
graph.title = "Songs Grouped By Rating"

ratings.keys.sort.each { |rating| graph.data rating, ratings[rating][:songs] }

graph.write "song-pie.png"
```

[Nokogiri]: http://www.nokogiri.org/
[plist]: https://github.com/bleything/plist
[XPath]: http://www.nokogiri.org/tutorials/searching_a_xml_html_document.html
This calls for [Nokogiri][] instead of [plist][], which gives me the opportunity to flex my amazing [XPath][]
skills. Nothing too complex. Thank goodness.

```
$ ruby graph-ratings.rb
Rating Songs Percent Duration
     0  8926   55.2% 24:13:00:24
     1   254    1.6% 00:19:49:30
     2   984    6.1% 02:21:42:54
     3  3932   24.3% 10:08:49:09
     4  1716   10.6% 04:10:50:01
     5   370    2.3% 00:23:16:01
```

How about that pretty picture?

{{< show-figure image="july-rhythmbox-song-pie.png" description="The song pie for July" >}}

I've made progress since graphing my [iTunes ratings][] in July. It looks less like Pac Man now.
