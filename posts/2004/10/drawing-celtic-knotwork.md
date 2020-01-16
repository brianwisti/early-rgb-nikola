---
aliases:
- /coolnamehere/2004/10/01_drawing-celtic-knotwork.html
- /post/2004/drawing-celtic-knotwork/
categories:
- coolnamehere
date: 2004-10-01T00:00:00Z
tags:
- ruby
- learn
title: Drawing Celtic Knotwork
type: post
updated: 2009-07-11T00:00:00Z
year: '2004'
---

Thanks to everybody for the positive feedback on the first MIRE. I still have
your attention, so I'll move on to my next exercise. This one is a little more
involved than the first, but bear with me - the results should be worth it.
<!--more-->

## The Problem

I have been a big fan of Celtic knotwork for many years, and have been drawing
it myself as an occasional distraction for most of that time.
I don't think I'm very good at it, but I've occasionally made myself proud.
Heck, I've even designed a couple tattoos for folks, making a few bucks in the
process. Any time you can profit from your hobbies is good. Any time somebody
likes your work so much that they want it embedded in their skin with a sharp
needle is also good.

My preferred technique has always been manual and therefore labor-intensive.
You lay out a grid, block out your major areas, draw your knotwork paths,
and then embellish a little for personality. It's simple and repetitive, and I
like it that way. There's a meditative element to such things which can't be
ignored. Still, I'm here to write a programming exercise, not to wax eloquently
about the virtues of being hunched over a sheet of paper for hours at a time.

Any time a geek hears the phrase "simple and repetitive," the geek's mind
turns to ways of automating the task being described. Well, *this* geek's mind
does. I wonder how hard it would be to write a Ruby program which 
could, given some dimensions by the user, create a simple knotwork panel of
the desired size and then write that panel to an image file?

## Finding a Solution

As it turns out, somebody else has already solved a fair chunk of the problem.
Andy Sloss's book ["How to Draw Celtic Knotwork: A Practical 
Guide"](https://www.goodreads.com/book/show/2762386-how-to-draw-celtic-knotwork)
provides a detailed overview of his approach, which essentially boils down to arranging a
set of image tiles on a grid so that the end result looks like an attractive
knotwork image. He's even gone so far as to provide each of the tiles that
can be used in his system. 

### The Plan

This project is a little more complicated than the last MIRE, so I want to step
through it a little more carefully. Actually, it's not more complicated. It's
just that less of the work has already been done for me. Instead of jumping
right into creating bitmap images on the fly, I'm going to use
[ASCII art](http://en.wikipedia.org/wiki/ASCII_art) to create my knotwork at first.

Let's step through what we'll be doing later in code. Here is a collection of
image tiles arranged in a grid.

    . . . . x x x x x  x x . . . . . x x  x x x x x . . . .
    . . . . x . . . .  . . x x . x x . .  . . . . x . . . .
    . . . . x . . . x  . . . . x . . . .  x . . . x . . . .
    . . . . x . . x .  x x . . . x . x x  . x . . x . . . .
    . . . . x . . x .  . . x . . . x . .  . x . . x . . . .
    . . . . . x . . x  x . . . x . . . x  x . . x . . . . .
    . . . . . x . . x  . . . x . x . . x  . . . x . . . . .
    . . . . . . x x .  . . x . . . x x .  . . x . . . . . .
    
    . . . . . . x . .  . . x . . . x . .  . x x . . . . . .
    . . . . . x . . .  . x . x . x . . .  x . . x . . . . .
    . . . . . x . . .  x . . . x . . . x  x . . x . . . . .
    . . . . x . . . x  . x . . . x . x .  . x . . x . . . .
    . . . . x . . x .  . . x . . . x . .  . x . . x . . . .
    . . . . x . . x .  . x . x . . . x .  . x . . x . . . .
    . . . . . x . . x  x . . . x . . . x  x . . x . . . . .
    . . . . . x . . x  . . . x . x . x .  . . . x . . . . .
    . . . . . . x x .  . . x . . . x . .  . . x . . . . . .
    
    . . . . . . x . .  . x x . . . x . .  . x x . . . . . .
    . . . . . x . . .  x . . x . x . . .  x . . x . . . . .
    . . . . . x . . x  x . . . x . . . x  x . . x . . . . .
    . . . . x . . x .  . x . . . x . x .  . x . . x . . . .
    . . . . x . . x .  . . x . . . x . .  . x . . x . . . .
    . . . . x . . . x  x x . x . . . x x  x . . . x . . . .
    . . . . x . . . .  . . . . x . . . .  . . . . x . . . .
    . . . . x . . . .  . . x x . x x . .  . . . . x . . . .
    . . . . x x x x x  x x . . . . . x x  x x x x x . . . .

Squish them together into one big image, and guess what? We have a knot!

    . . . . x x x x x x x . . . . . x x x x x x x . . . .
    . . . . x . . . . . . x x . x x . . . . . . x . . . .
    . . . . x . . . x . . . . x . . . . x . . . x . . . .
    . . . . x . . x . x x . . . x . x x . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . . x . . x . . . x . x . . x . . . x . . . . .
    . . . . . . x x . . . x . . . x x . . . x . . . . . .
    . . . . . . x . . . . x . . . x . . . x x . . . . . .
    . . . . . x . . . . x . x . x . . . x . . x . . . . .
    . . . . . x . . . x . . . x . . . x x . . x . . . . .
    . . . . x . . . x . x . . . x . x . . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . x . . x . x . . . x . . x . . x . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . . x . . x . . . x . x . x . . . . x . . . . .
    . . . . . . x x . . . x . . . x . . . . x . . . . . .
    . . . . . . x . . . x x . . . x . . . x x . . . . . .
    . . . . . x . . . x . . x . x . . . x . . x . . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . x . . x . . x . . . x . x . . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . . x x x . x . . . x x x . . . x . . . .
    . . . . x . . . . . . . . x . . . . . . . . x . . . .
    . . . . x . . . . . . x x . x x . . . . . . x . . . .
    . . . . x x x x x x x . . . . . x x x x x x x . . . .

You don't quite see it? Well, squint a little and tilt your head a bit. Still
nothing? Just bear with me. We will get to actual pictures soon, I promise.

Okay, let's find a way to automate this process.

### Turning the Plan Into Code

This works, doesn't it?

``` ruby
knot =<<HERE
     . . . . x x x x x x x . . . . . x x x x x x x . . . .
     . . . . x . . . . . . x x . x x . . . . . . x . . . .
     . . . . x . . . x . . . . x . . . . x . . . x . . . .
     . . . . x . . x . x x . . . x . x x . x . . x . . . .
     . . . . x . . x . . . x . . . x . . . x . . x . . . .
     . . . . . x . . x x . . . x . . . x x . . x . . . . .
     . . . . . x . . x . . . x . x . . x . . . x . . . . .
     . . . . . . x x . . . x . . . x x . . . x . . . . . .
     . . . . . . x . . . . x . . . x . . . x x . . . . . .
     . . . . . x . . . . x . x . x . . . x . . x . . . . .
     . . . . . x . . . x . . . x . . . x x . . x . . . . .
     . . . . x . . . x . x . . . x . x . . x . . x . . . .
     . . . . x . . x . . . x . . . x . . . x . . x . . . .
     . . . . x . . x . . x . x . . . x . . x . . x . . . .
     . . . . . x . . x x . . . x . . . x x . . x . . . . .
     . . . . . x . . x . . . x . x . x . . . . x . . . . .
     . . . . . . x x . . . x . . . x . . . . x . . . . . .
     . . . . . . x . . . x x . . . x . . . x x . . . . . .
     . . . . . x . . . x . . x . x . . . x . . x . . . . .
     . . . . . x . . x x . . . x . . . x x . . x . . . . .
     . . . . x . . x . . x . . . x . x . . x . . x . . . .
     . . . . x . . x . . . x . . . x . . . x . . x . . . .
     . . . . x . . . x x x . x . . . x x x . . . x . . . .
     . . . . x . . . . . . . . x . . . . . . . . x . . . .
     . . . . x . . . . . . x x . x x . . . . . . x . . . .
     . . . . x x x x x x x . . . . . x x x x x x x . . . .
HERE
puts knot
```

I know, "Ha ha, very funny. You are so clever and witty. We are being 
sarcastic, if you didn't guess, Mister Writer." I know that this is cheating,
but it *works* doesn't it? This would be good enough if all you wanted
was some sort of ASCII art knot.

Then again, Laziness taken too far does become plain old laziness. This isn't
good enough for any of us. The idea is to be able to draw a knotwork panel of 
any size that we want.

Let's look at the nouns we've used when describing the problem:

> We want to create a knotwork panel by arranging tiles on a grid, then 
> merging them into a single image.

* knotwork panel - *I threw the adjective in for a little descriptiveness*
* grid
* tile
* image

I think these nouns make a good start for the class names in our program.

``` ruby
class KnotworkPanel
end

class Grid
end

class Tile
end

class Image
end
```

[Zenspider](http://www.zenspider.com/) once mentioned a style of 
commenting classes that was like the classes were describing themselves in 
the first person. I don't know why, but I really liked that concept. I've 
stuck with it in a lot of my own code ever since.

``` ruby
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
end

# I am a 2-dimensional collection of tiles. I know where each of my Tiles are located,
# and can describe them as if they were a single large entity.
class Grid
end

# I am a lovely Celtic knotwork panel. I know my dimensions, and can output myself
# as ASCII art.
class KnotworkPanel
end
```

Now I know each of the major objects in this program, and the duties that they must
fill. It's time to blaze through the highlights of writing the code. For convenience, we
can put the application code and the testing code in the same file for now.

## Building a Tile

The simplest element of our description is the Tile. I decided that a Tile 
would be a two dimensional chunk of characters that would let you set or get 
any point in that space. Remember that this isn't the only way we could have 
done things. You could also describe the lines and curves in the tile, or the 
colors, transparency, and whatever else the crazy kids are coming up with 
these days. This is my first drawing program, though, and I want to keep it as 
simple as I can. So I'm going with the bitmap idea. The tile images in the 
Sloss book are provided in different sizes. Let's go with 9x9. It's small and 
manageable without being too small to see.

``` ruby
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize()
    @pixels = []
    (0..8).each { 
      row = []
      (0..8).each { row << nil }
      @pixels << row
    }
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|" 
      }
      str += "\n"
    }
    return str
  end
end
  
#####
# Test code
#####
  
require 'test/unit'
  
class TC_Tile < Test::Unit::TestCase
  def setup
    @@tile = Tile.new()
  end
  
  def test_pixels
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "By default, any pixel in a Tile is blank")
    assert(@@tile.set(0, 0), 
      "Use Tile#set(row, col) to set a pixel at coordinates (row, col)")
    assert(@@tile.is_set?(0, 0), 
      "A pixel (row, col) is set after Tile#set(row, col) has been called")
    assert(@@tile.unset(0, 0), 
      "Use Tile#unset(row, col) to clear a pixel at coordinates (row, col)")
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "An unset pixel has no set value")
    @@tile.set(1, 1)
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "Setting one pixel has no effect on other pixels in a Tile")
    assert(@@tile.is_set?(1, 1), 
      "Tile remembers the set status of each pixel in its confines.")
    source_string =<<HERE
      x . . . . . . . x
      . x . . . . . x .
      . . x . . . x . .
      . . . x . x . . .
      . . . . x . . . .
      . . . x . x . . .
      . . x . . . x . .
      . x . . . . . x .
      x . . . . . . . x
HERE

    source_string.gsub!(/^\s+/m, '')
    assert(@@tile.set_from_string(source_string),
      "You can use ASCII art strings to set the pixels in a Tile")
    assert(@@tile.is_set?(0, 0))
    assert(@@tile.is_set?(1, 0))
    assert_equal('x', @@tile.at(0, 0),
      "A Tile remembers the value assigned, if given, during " \
      "Tile#set(row, col, val)")
  end
end
```

I'm told this is [Test Driven Development](http://www.agiledata.org/essays/tdd.html), 
where you write the tests for your code as you are writing the code itself. A 
little *before* the code itself, actually. TDD is useful for any non-trivial 
programming task. You have the tests there right from the beginning to describe 
what your classes are supposed to be able to do. Because TDD is based on lots 
of tiny changes being applied rapidly over time, I decided it would be 
tedious to describe that process to you at each little step.  Instead, we stop 
and take a snapshot as we get each major stage accomplished. Like that code 
sample up there. It's really where I'm at right about now. See: there's the 
class definition, a couple of very basic accessors, and the ability to set all 
the pixels of a Tile at once from a String.

Now that the Tile is pretty much doing everything I want it to, let's move on 
to the Grid.

## Putting the Tile in a Grid

I want to hurry on to making pictures, so let's rush through the Grid part.

That's easy enough, actually. We only need to be able to do a few simple 
things with a Grid: 

* Create it at a set size.
* Add a Tile somewhere in the Grid.
* Read each individual pixel of the Grid transparently.

And here's the code.

``` ruby
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize(str = nil)
    @pixels = []
    (0..8).each { 
      row = []
      (0..8).each { row << nil }
      @pixels << row
    }
    
    if str then
      set_from_string(str)
    end
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|" 
      }
      str += "\n"
    }
    return str
  end
end

# I am an arranged collection of Tiles. I know how to add and remove
# Tiles along a 2-d grid, and can also present myself as if I were a single
# large Tile.
class Grid
  def initialize(rows, columns)
    @tile_size = 9
    @rows      = rows
    @columns   = columns
    @pixels    = Array.new(rows*@tile_size) { |i|
      Array.new(columns*@tile_size)
    }
  end
  
  def set_tile(row, column, tile)
    pixel_origin_x = row * @tile_size
    pixel_origin_y = column * @tile_size
    (0...@tile_size).each { |tile_x|
      x = pixel_origin_x + tile_x
      (0...@tile_size).each { |tile_y|
        y = pixel_origin_y + tile_y
        @pixels[x][y] = tile.at(tile_x, tile_y)
      }
    }
  end
  
  def at(row, column)
    return @pixels[row][column]
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += row.join(' ')
      str += "\n"
    }
    
    return str
  end
  
end


#####
# Test code
#####
$source_string =<<HERE
          x . . . . . . . x
          . x . . . . . x .
          . . x . . . x . .
          . . . x . x . . .
          . . . . x . . . .
          . . . x . x . . .
          . . x . . . x . .
          . x . . . . . x .
          x . . . . . . . x
HERE
$source_string.gsub!(/^\s+/m, '')

require 'test/unit'

class TC_Tile < Test::Unit::TestCase
  def setup
    @@tile = Tile.new()
  end
  
  def test_pixels
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "By default, any pixel in a Tile is blank")
    assert(@@tile.set(0, 0), 
           "Use Tile#set(row, col) to set a pixel at coordinates (row, col)")
    assert(@@tile.is_set?(0, 0), 
           "A pixel (row, col) is set after Tile#set(row, col) has been called")
    assert(@@tile.unset(0, 0), 
           "Use Tile#unset(row, col) to clear a pixel at coordinates (row, col)")
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "An unset pixel has no set value")
    @@tile.set(1, 1)
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "Setting one pixel has no effect on other pixels in a Tile")
    assert(@@tile.is_set?(1, 1), 
           "Tile remembers the set status of each pixel in its confines.")
    
    assert(@@tile.set_from_string($source_string),
           "You can use ASCII art strings to set the pixels in a Tile")
    assert(@@tile.is_set?(0, 0))
    assert(@@tile.is_set?(1, 0))
    assert_equal('x', @@tile.at(0, 0),
                 "A Tile remembers the value assigned, if given, " \
                 "during Tile#set(row, col, val)")
  end
end

class TC_Grid < Test::Unit::TestCase
  def test_simple_grid
    grid = Grid.new(1, 1)
    tile = Tile.new($source_string)
    grid.set_tile(0, 0, tile)
    assert_equal("x", grid.at(0, 0),
                 "Use Grid#pixel_at(row, col) to access pixel at " \
                 "(row, col) distance from upper left corner")
    assert_equal($source_string, grid.to_s)
  end
  
  def test_large_grid
    grid = Grid.new(1, 2)
    tile1 = Tile.new($source_string)
    tile2 = Tile.new($source_string)
    grid.set_tile(0, 0, tile1)
    grid.set_tile(0, 1, tile2)
    assert_equal("x", grid.at(0, 0))
    assert_equal("x", grid.at(0, 9),
                 "Grid#pixel_at uses whole grid as coordinate system")
    expected_output =<<HERE
          x . . . . . . . x x . . . . . . . x
          . x . . . . . x . . x . . . . . x .
          . . x . . . x . . . . x . . . x . .
          . . . x . x . . . . . . x . x . . .
          . . . . x . . . . . . . . x . . . .
          . . . x . x . . . . . . x . x . . .
          . . x . . . x . . . . x . . . x . .
          . x . . . . . x . . x . . . . . x .
          x . . . . . . . x x . . . . . . . x
HERE

    expected_output.gsub!(/^\s+/, '')
    assert_equal(expected_output, grid.to_s)
  end
end

class TestKnotworkPanel < Test::Unit::TestCase
end
```

There, that's another fifteen minutes of coding done. Yes, the combination of TDD and Ruby makes it about this easy to write a program.

## Using the Grid to Make a KnotworkPanel

Things get a little more complex now, because we're on to creating a 
KnotworkPanel. Every KnotworkPanel uses a specific set of predefined 
tiles - *thanks again to Andy Sloss for going to the trouble of defining 
them* - which I will store as class variables. I would probably store them in 
a different file if I wanted to include *every* Tile defined in Sloss's book, 
but that's more than I want to chew on today.

Certain Tiles must go in certain locations of the KnotworkPanel's Grid, such 
as the corners and edges, and we have to remember this in our tests. Ah, let's 
just cut and paste the source strings and squish them together so that they 
look like what we're aiming for. That's probably the easiest test for now.

For a while, my problem was that I was copying and pasting incorrectly. Don't 
ask me how I pull this stuff off. I'm just special, I guess.  The test results 
would end up spewing out "Expected "... a really long chain of `x` and `.` 
characters, " but got " ... a really long chain of `x` and `.` characters, 
almost identical to the first chain. My solution? Test each row of output, 
that way I see exactly which line was one character off.

``` ruby
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize(str = nil)
    @pixels = []
    (0..8).each { 
      row = []
      (0..8).each { row << nil }
      @pixels << row
    }
    
    if str then
      set_from_string(str)
    end
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|" 
      }
      str += "\n"
    }
    return str
  end
end

# I am an arranged collection of Tiles. I know how to add and remove
# Tiles along a 2-d grid, and can also present myself as if I were a single
# large Tile.
class Grid
  def initialize(rows, columns)
    @tile_size = 9
    @rows      = rows
    @columns   = columns
    @pixels    = Array.new(rows*@tile_size) { |i|
      Array.new(columns*@tile_size)
    }
  end
  
  def set_tile(row, column, tile)
    if row >= @rows or column >= @columns then
      raise ArgumentError, \
      "set_tile at #{row}, #{column} outside of Grid area " \
      "(#{@rows}, #{@columns})"
    end
    
    pixel_origin_x = row * @tile_size
    pixel_origin_y = column * @tile_size
    (0...@tile_size).each { |tile_x|
      x = pixel_origin_x + tile_x
      (0...@tile_size).each { |tile_y|
        y = pixel_origin_y + tile_y
        @pixels[x][y] = tile.at(tile_x, tile_y)
      }
    }
  end
  
  def at(row, column)
    return @pixels[row][column]
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += row.join(' ')
      str += "\n"
    }
    
    return str
  end
  
end

# I am a lovely Celtic knotwork panel. I know my dimensions, and can output myself
# as ASCII art.
class KnotworkPanel
  
  @@top_left = Tile.new(%{. . . . x x x x x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, ''))
      
  @@top      = Tile.new(%{x x . . . . . x x
                          . . x x . x x . .
                          . . . . x . . . .
                          x x . . . x . x x
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . . x
                          . . x . . . x x .}.gsub(/^\s+/, '')
                        )
      
  @@topright = Tile.new(%{x x x x x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x . . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
      
  @@left     = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, '')
                            )
      
  @@center   = Tile.new(%{. . x . . . x . .
                          . x . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . x .
                          . . x . . . x . .}.gsub(/^\s+/, '')
                        )
      
  @@right    = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
      
  @@bot_left = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . x . . . x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x x x x x}.gsub(/^\s+/, '')
                        )
  
  @@bottom   = Tile.new(%{. x x . . . x . .
                          x . . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          x x . x . . . x x
                          . . . . x . . . .
                          . . x x . x x . .
                          x x . . . . . x x}.gsub(/^\s+/, '')
                        )
  
  @@botright = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x x x x x . . . .}.gsub(/^\s+/, '')
                        )
      
  def initialize(rows, columns=rows)
    @row_size = rows + 2
    @col_size = columns + 2
    
    @grid = Grid.new(@row_size, @col_size)
    
    # Set the top row
    @grid.set_tile(0, 0, @@top_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(0, i, @@top)
    end
    @grid.set_tile(0, @col_size-1, @@topright)
    
    # Set the center rows.
    (1...@row_size-1).each do |i|
      @grid.set_tile(i, 0, @@left)
      (1...@col_size-1).each do |j|
        @grid.set_tile(i, j, @@center)
      end
      @grid.set_tile(i, @col_size-1, @@right)
    end
    
    # Set the bottom row
    @grid.set_tile(@row_size-1, 0, @@bot_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(@row_size-1, i, @@bottom)
    end
    @grid.set_tile(@row_size-1, @col_size-1, @@botright)
  end
  
  def to_aa()
    return @grid.to_s
  end
  
end

#####
# Test code
#####
$source_string =<<HERE
          x . . . . . . . x
          . x . . . . . x .
          . . x . . . x . .
          . . . x . x . . .
          . . . . x . . . .
          . . . x . x . . .
          . . x . . . x . .
          . x . . . . . x .
          x . . . . . . . x
HERE
$source_string.gsub!(/^\s+/m, '')
      
require 'test/unit'

class TC_Tile < Test::Unit::TestCase
  def setup
    @@tile = Tile.new()
  end
  
  def test_pixels
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "By default, any pixel in a Tile is blank")
    assert(@@tile.set(0, 0), 
           "Use Tile#set(row, col) to set a pixel at coordinates (row, col)")
    assert(@@tile.is_set?(0, 0), 
           "A pixel (row, col) is set after Tile#set(row, col) has been called")
    assert(@@tile.unset(0, 0), 
           "Use Tile#unset(row, col) to clear a pixel at coordinates (row, col)")
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "An unset pixel has no set value")
    @@tile.set(1, 1)
    assert_equal(nil, @@tile.is_set?(0, 0), 
                 "Setting one pixel has no effect on other pixels in a Tile")
    assert(@@tile.is_set?(1, 1), 
           "Tile remembers the set status of each pixel in its confines.")
    assert(@@tile.set_from_string($source_string),
           "You can use ASCII art strings to set the pixels in a Tile")
    assert(@@tile.is_set?(0, 0))
    assert(@@tile.is_set?(1, 0))
    assert_equal('x', @@tile.at(0, 0),
                 "A Tile remembers the value assigned, if given, " \
                 "during Tile#set(row, col, val)")
  end
end

class TC_Grid < Test::Unit::TestCase
  def test_simple_grid
    grid = Grid.new(1, 1)
    tile = Tile.new($source_string)
    grid.set_tile(0, 0, tile)
    assert_equal("x", grid.at(0, 0),
                 "Use Grid#pixel_at(row, col) to access pixel at (row, col)" \
                 "distance from upper left corner")
    assert_equal($source_string, grid.to_s)
    assert_raise(ArgumentError, "You cannot set a Tile outside of the Grid.") \
    { grid.set_tile(1, 1, tile) }
  end
  def test_large_grid
    grid = Grid.new(1, 2)
    tile1 = Tile.new($source_string)
    tile2 = Tile.new($source_string)
    grid.set_tile(0, 0, tile1)
    grid.set_tile(0, 1, tile2)
    assert_equal("x", grid.at(0, 0))
    assert_equal("x", grid.at(0, 9),
                 "Grid#pixel_at uses whole grid as coordinate system")
    expected_output =<<HERE
          x . . . . . . . x x . . . . . . . x
          . x . . . . . x . . x . . . . . x .
          . . x . . . x . . . . x . . . x . .
          . . . x . x . . . . . . x . x . . .
          . . . . x . . . . . . . . x . . . .
          . . . x . x . . . . . . x . x . . .
          . . x . . . x . . . . x . . . x . .
          . x . . . . . x . . x . . . . . x .
          x . . . . . . . x x . . . . . . . x
HERE
    expected_output.gsub!(/^\s+/, '')
    assert_equal(expected_output, grid.to_s)
  end
end

class TestKnotworkPanel < Test::Unit::TestCase
  def test_ascii
    panel = KnotworkPanel.new(1)
    ascii_output_1 =<<HERE
          . . . . x x x x x x x . . . . . x x x x x x x . . . .
          . . . . x . . . . . . x x . x x . . . . . . x . . . .
          . . . . x . . . . . . . . x . . . . . . . . x . . . .
          . . . . x . . . x x x . . . x . x x x . . . x . . . .
          . . . . x . . x . . . x . . . x . . . x . . x . . . .
          . . . . x . . x . . x . x . . . x . . x . . x . . . .
          . . . . . x . . x x . . . x . . . x x . . x . . . . .
          . . . . . x . . x . . . x . x . . x . . . x . . . . .
          . . . . . . x x . . . x . . . x x . . . x . . . . . .
          . . . . . . x . . . . x . . . x . . . x x . . . . . .
          . . . . . x . . . . x . x . x . . . x . . x . . . . .
          . . . . . x . . . x . . . x . . . x x . . x . . . . .
          . . . . x . . . x . x . . . x . x . . x . . x . . . .
          . . . . x . . x . . . x . . . x . . . x . . x . . . .
          . . . . x . . x . . x . x . . . x . . x . . x . . . .
          . . . . . x . . x x . . . x . . . x x . . x . . . . .
          . . . . . x . . x . . . x . x . x . . . . x . . . . .
          . . . . . . x x . . . x . . . x . . . . x . . . . . .
          . . . . . . x . . . x x . . . x . . . x x . . . . . .
          . . . . . x . . . x . . x . x . . . x . . x . . . . .
          . . . . . x . . x x . . . x . . . x x . . x . . . . .
          . . . . x . . x . . x . . . x . x . . x . . x . . . .
          . . . . x . . x . . . x . . . x . . . x . . x . . . .
          . . . . x . . . x x x . x . . . x x x . . . x . . . .
          . . . . x . . . . . . . . x . . . . . . . . x . . . .
          . . . . x . . . . . . x x . x x . . . . . . x . . . .
          . . . . x x x x x x x . . . . . x x x x x x x . . . .
HERE
    
    ascii_output_1.gsub!(/^\s+/, '')
    real_output = panel.to_aa.split("\n")
    ascii_output_1.split("\n").each_with_index do |line, i|
      assert_equal(line, real_output[i],
                   "line #{i} doesn't match")
    end
    
  end
  
  def test_large_panels
    ascii_output_1 =<<HERE
        . . . . x x x x x x x . . . . . x x x x x x x . . . .
        . . . . x . . . . . . x x . x x . . . . . . x . . . .
        . . . . x . . . . . . . . x . . . . . . . . x . . . .
        . . . . x . . . x x x . . . x . x x x . . . x . . . .
        . . . . x . . x . . . x . . . x . . . x . . x . . . .
        . . . . x . . x . . x . x . . . x . . x . . x . . . .
        . . . . . x . . x x . . . x . . . x x . . x . . . . .
        . . . . . x . . x . . . x . x . . x . . . x . . . . .
        . . . . . . x x . . . x . . . x x . . . x . . . . . .
        . . . . . . x . . . . x . . . x . . . x x . . . . . .
        . . . . . x . . . . x . x . x . . . x . . x . . . . .
        . . . . . x . . . x . . . x . . . x x . . x . . . . .
        . . . . x . . . x . x . . . x . x . . x . . x . . . .
        . . . . x . . x . . . x . . . x . . . x . . x . . . .
        . . . . x . . x . . x . x . . . x . . x . . x . . . .
        . . . . . x . . x x . . . x . . . x x . . x . . . . .
        . . . . . x . . x . . . x . x . x . . . . x . . . . .
        . . . . . . x x . . . x . . . x . . . . x . . . . . .
        . . . . . . x . . . . x . . . x . . . x x . . . . . .
        . . . . . x . . . . x . x . x . . . x . . x . . . . .
        . . . . . x . . . x . . . x . . . x x . . x . . . . .
        . . . . x . . . x . x . . . x . x . . x . . x . . . .
        . . . . x . . x . . . x . . . x . . . x . . x . . . .
        . . . . x . . x . . x . x . . . x . . x . . x . . . .
        . . . . . x . . x x . . . x . . . x x . . x . . . . .
        . . . . . x . . x . . . x . x . x . . . . x . . . . .
        . . . . . . x x . . . x . . . x . . . . x . . . . . .
        . . . . . . x . . . x x . . . x . . . x x . . . . . .
        . . . . . x . . . x . . x . x . . . x . . x . . . . .
        . . . . . x . . x x . . . x . . . x x . . x . . . . .
        . . . . x . . x . . x . . . x . x . . x . . x . . . .
        . . . . x . . x . . . x . . . x . . . x . . x . . . .
        . . . . x . . . x x x . x . . . x x x . . . x . . . .
        . . . . x . . . . . . . . x . . . . . . . . x . . . .
        . . . . x . . . . . . x x . x x . . . . . . x . . . .
        . . . . x x x x x x x . . . . . x x x x x x x . . . .
HERE
        
    ascii_output_1.gsub!(/^\s+/, '')
    panel = KnotworkPanel.new(2, 1)
    real_output = panel.to_aa.split("\n")
    ascii_output_1.split("\n").each_with_index do |line, i|
      assert_equal(line, real_output[i],
                   "line #{i} doesn't match")
    end
  end
  
end
```
  
Yeah, that works. Let's move on.

<aside>
Wait. This is me from the future, editing this page. KnotworkPanel's 
initializer kinda bugs me. It's fine for what it does, but how's the average 
person supposed to know that <code>KnotworkPanel.new(1,2)</code> actually 
creates a KnotworkPanel with dimensions of 3x5, including the border?  Really, 
this is why you need some person to represent the customer or a user besides 
yourself whenever you want to write code for other people to use. I could 
change the initializer, but I really want to get the article out so the geeks 
of the world can point and laugh at my mistakes. For now, just remember that 
the dimensions sent to the initializer don't include the bordering tiles. So 
if you want a 5x5 panel, you'll have to call <code>KnotworkPanel.new(3, 3)</code>. 
Man, that's ugly. Let's make fixing that an exercise at the end of the article, okay?
</aside>

## Creating an Image of the KnotworkPanel

I bet you feel really cheated by now. I've been going on for all this time 
about celtic knotwork and drawing pictures with the computer, and all you've 
seen is a bunch of dots and crosses that kind of look like a picture if you 
go cross-eyed for a second. You can cheer up, folks, because you've finished 
the boring part. Now we want to make a real live picture!

But how are we going to do it? You know that I'm *not* about to go making my 
own image creation library for a little project like this - or any other 
project, if I can help it. There's no need, either, because there are at least 
two great choices available:

* [Ruby/GD](http://raa.ruby-lang.org/project/ruby-gd/), a wrapper for the 
  [GD](http://www.boutell.com/gd/) library.
* [RMagick](http://rmagick.rubyforge.org/), a wrapper for the 
  [ImageMagick](http://imagemagick.org/) library.

Each of these options are Ruby-based interfaces to very powerful image 
generation and manipulation libraries which have been around for ... ages, 
really. Either one would provide more than enough muscle to squish bitmaps 
together. 

Since it's a coin-toss for either library based on utility, we have to move on 
to the next measure: documentation. Ruby/GD might have some great documents 
hidden around somewhere, but I sure can't find them. RMagick, on the other 
hand, has a useful manual [accessible 
online](http://www.simplesystems.org/RMagick/doc/index.html). See, I've 
started to learn that most great programmers aren't really all-knowing - they 
just know how to look stuff up quickly. If I have a good manual handy, then 
that makes it easier to become a great programmer. At least I can make 
myself look useful...

``` ruby
require 'RMagick'
include Magick
  
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize(str = nil)
    @pixels = []
    (0..8).each { 
      row = []
      (0..8).each { row << nil }
      @pixels << row
    }
    
    if str then
      set_from_string(str)
    end
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|" 
      }
      str += "\n"
    }
    return str
  end
end
  
# I am an arranged collection of Tiles. I know how to add and remove
# Tiles along a 2-d grid, and can also present myself as if I were a single
# large Tile.
class Grid
  def initialize(rows, columns)
    @tile_size = 9
    @rows      = rows
    @columns   = columns
    @pixels    = Array.new(rows*@tile_size) { |i|
      Array.new(columns*@tile_size)
    }
  end
  
  def set_tile(row, column, tile)
    if row >= @rows or column >= @columns then
      raise ArgumentError, \
      "set_tile at #{row}, #{column} outside of Grid area " \
      "(#{@rows}, #{@columns})"
    end
    
    pixel_origin_x = row * @tile_size
    pixel_origin_y = column * @tile_size
    (0...@tile_size).each { |tile_x|
      x = pixel_origin_x + tile_x
      (0...@tile_size).each { |tile_y|
        y = pixel_origin_y + tile_y
        @pixels[x][y] = tile.at(tile_x, tile_y)
      }
    }
  end
  
  def at(row, column)
    return @pixels[row][column]
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += row.join(' ')
      str += "\n"
    }
    
    return str
  end
  
end
  
# I am a lovely Celtic knotwork panel. I know my dimensions, and can 
# output myself as ASCII art.
class KnotworkPanel
  @@top_left = Tile.new(%{. . . . x x x x x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, ''))
  
  @@top      = Tile.new(%{x x . . . . . x x
                          . . x x . x x . .
                          . . . . x . . . .
                          x x . . . x . x x
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . . x
                          . . x . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@topright = Tile.new(%{x x x x x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x . . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@left     = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@center   = Tile.new(%{. . x . . . x . .
                          . x . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . x .
                          . . x . . . x . .}.gsub(/^\s+/, '')
                        )
  
  @@right    = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@bot_left = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . x . . . x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x x x x x}.gsub(/^\s+/, '')
                        )
  
  @@bottom   = Tile.new(%{. x x . . . x . .
                          x . . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          x x . x . . . x x
                          . . . . x . . . .
                          . . x x . x x . .
                          x x . . . . . x x}.gsub(/^\s+/, '')
                        )
  
  @@botright = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x x x x x . . . .}.gsub(/^\s+/, '')
                        )
  
  def initialize(rows, columns=rows)
    @row_size = rows + 2
    @col_size = columns + 2
    
    @grid = Grid.new(@row_size, @col_size)
    
    # Set the top row
    @grid.set_tile(0, 0, @@top_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(0, i, @@top)
    end
    @grid.set_tile(0, @col_size-1, @@topright)
    
    # Set the center rows.
    (1...@row_size-1).each do |i|
      @grid.set_tile(i, 0, @@left)
      (1...@col_size-1).each do |j|
        @grid.set_tile(i, j, @@center)
      end
      @grid.set_tile(i, @col_size-1, @@right)
    end
    
    # Set the bottom row
    @grid.set_tile(@row_size-1, 0, @@bot_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(@row_size-1, i, @@bottom)
    end
    @grid.set_tile(@row_size-1, @col_size-1, @@botright)
  end
  
  def to_aa()
    return @grid.to_s
  end
  
  def to_image()
    
    filename = "panel-#{@row_size}x#{@col_size}.png"
    
    max_x = 9 * @row_size
    max_y = 9 * @col_size
    
    image = Image.new(max_x, max_y) { self.background_color = "white" }
    (0...max_y).each do |y|
      (0...max_x).each do |x|
        pixel = @grid.at(x, y)
        if pixel == "x" then
          image.pixel_color(x, y, "black")
        end
      end
    end
    image.write(filename)
    
  end
  
end
  
#####
# Test code
#####
$source_string =<<HERE
      x . . . . . . . x
      . x . . . . . x .
      . . x . . . x . .
      . . . x . x . . .
      . . . . x . . . .
      . . . x . x . . .
      . . x . . . x . .
      . x . . . . . x .
      x . . . . . . . x
HERE
$source_string.gsub!(/^\s+/m, ")
  
require 'test/unit'
  
class TC_Tile < Test::Unit::TestCase
  def setup
    @@tile = Tile.new()
  end
  
  def test_pixels
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "By default, any pixel in a Tile is blank")
    assert(@@tile.set(0, 0), 
      "Use Tile#set(row, col) to set a pixel at coordinates (row, col)")
    assert(@@tile.is_set?(0, 0), 
      "A pixel (row, col) is set after Tile#set(row, col) has been called")
    assert(@@tile.unset(0, 0), 
      "Use Tile#unset(row, col) to clear a pixel at coordinates (row, col)")
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "An unset pixel has no set value")
    @@tile.set(1, 1)
    assert_equal(nil, @@tile.is_set?(0, 0), 
      "Setting one pixel has no effect on other pixels in a Tile")
    assert(@@tile.is_set?(1, 1), 
      "Tile remembers the set status of each pixel in its confines.")
    
    assert(@@tile.set_from_string($source_string),
      "You can use ASCII art strings to set the pixels in a Tile")
    assert(@@tile.is_set?(0, 0))
    assert(@@tile.is_set?(1, 0))
    assert_equal('x', @@tile.at(0, 0),
      "A Tile remembers the value assigned, if given, " \
      "during Tile#set(row, col, val)")
  end
end
  
class TC_Grid < Test::Unit::TestCase
  def test_simple_grid
    grid = Grid.new(1, 1)
    tile = Tile.new($source_string)
    grid.set_tile(0, 0, tile)
    assert_equal("x", grid.at(0, 0),
      "Use Grid#pixel_at(row, col) to access pixel at (row, col) " \
      "distance from upper left corner")
    assert_equal($source_string, grid.to_s)
    assert_raise(ArgumentError, "You cannot set a Tile outside of the Grid." { 
                   grid.set_tile(1, 1, tile) 
                 }
  end
  def test_large_grid
    grid = Grid.new(1, 2)
    tile1 = Tile.new($source_string)
    tile2 = Tile.new($source_string)
    grid.set_tile(0, 0, tile1)
    grid.set_tile(0, 1, tile2)
    assert_equal("x", grid.at(0, 0))
    assert_equal("x", grid.at(0, 9),
                 "Grid#pixel_at uses whole grid as coordinate system")
    expected_output =<<HERE
      x . . . . . . . x x . . . . . . . x
      . x . . . . . x . . x . . . . . x .
      . . x . . . x . . . . x . . . x . .
      . . . x . x . . . . . . x . x . . .
      . . . . x . . . . . . . . x . . . .
      . . . x . x . . . . . . x . x . . .
      . . x . . . x . . . . x . . . x . .
      . x . . . . . x . . x . . . . . x .
      x . . . . . . . x x . . . . . . . x
HERE
    expected_output.gsub!(/^\s+/, ")
    assert_equal(expected_output, grid.to_s)
  end
end
  
class TestKnotworkPanel < Test::Unit::TestCase
  def test_ascii
    panel = KnotworkPanel.new(1)
    ascii_output_1 =<<HERE
      . . . . x x x x x x x . . . . . x x x x x x x . . . .
      . . . . x . . . . . . x x . x x . . . . . . x . . . .
      . . . . x . . . . . . . . x . . . . . . . . x . . . .
      . . . . x . . . x x x . . . x . x x x . . . x . . . .
      . . . . x . . x . . . x . . . x . . . x . . x . . . .
      . . . . x . . x . . x . x . . . x . . x . . x . . . .
      . . . . . x . . x x . . . x . . . x x . . x . . . . .
      . . . . . x . . x . . . x . x . . x . . . x . . . . .
      . . . . . . x x . . . x . . . x x . . . x . . . . . .
      . . . . . . x . . . . x . . . x . . . x x . . . . . .
      . . . . . x . . . . x . x . x . . . x . . x . . . . .
      . . . . . x . . . x . . . x . . . x x . . x . . . . .
      . . . . x . . . x . x . . . x . x . . x . . x . . . .
      . . . . x . . x . . . x . . . x . . . x . . x . . . .
      . . . . x . . x . . x . x . . . x . . x . . x . . . .
      . . . . . x . . x x . . . x . . . x x . . x . . . . .
      . . . . . x . . x . . . x . x . x . . . . x . . . . .
      . . . . . . x x . . . x . . . x . . . . x . . . . . .
      . . . . . . x . . . x x . . . x . . . x x . . . . . .
      . . . . . x . . . x . . x . x . . . x . . x . . . . .
      . . . . . x . . x x . . . x . . . x x . . x . . . . .
      . . . . x . . x . . x . . . x . x . . x . . x . . . .
      . . . . x . . x . . . x . . . x . . . x . . x . . . .
      . . . . x . . . x x x . x . . . x x x . . . x . . . .
      . . . . x . . . . . . . . x . . . . . . . . x . . . .
      . . . . x . . . . . . x x . x x . . . . . . x . . . .
      . . . . x x x x x x x . . . . . x x x x x x x . . . .
HERE
    
    ascii_output_1.gsub!(/^\s+/, '')
    real_output = panel.to_aa.split("\n")
    ascii_output_1.split("\n").each_with_index do |line, i|
      assert_equal(line, real_output[i],
                   "line #{i} doesn't match")
    end
    
  end
  
  def test_large_panels
    ascii_output_1 =<<HERE
    . . . . x x x x x x x . . . . . x x x x x x x . . . .
    . . . . x . . . . . . x x . x x . . . . . . x . . . .
    . . . . x . . . . . . . . x . . . . . . . . x . . . .
    . . . . x . . . x x x . . . x . x x x . . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . x . . x . x . . . x . . x . . x . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . . x . . x . . . x . x . . x . . . x . . . . .
    . . . . . . x x . . . x . . . x x . . . x . . . . . .
    . . . . . . x . . . . x . . . x . . . x x . . . . . .
    . . . . . x . . . . x . x . x . . . x . . x . . . . .
    . . . . . x . . . x . . . x . . . x x . . x . . . . .
    . . . . x . . . x . x . . . x . x . . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . x . . x . x . . . x . . x . . x . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . . x . . x . . . x . x . x . . . . x . . . . .
    . . . . . . x x . . . x . . . x . . . . x . . . . . .
    . . . . . . x . . . . x . . . x . . . x x . . . . . .
    . . . . . x . . . . x . x . x . . . x . . x . . . . .
    . . . . . x . . . x . . . x . . . x x . . x . . . . .
    . . . . x . . . x . x . . . x . x . . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . x . . x . x . . . x . . x . . x . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . . x . . x . . . x . x . x . . . . x . . . . .
    . . . . . . x x . . . x . . . x . . . . x . . . . . .
    . . . . . . x . . . x x . . . x . . . x x . . . . . .
    . . . . . x . . . x . . x . x . . . x . . x . . . . .
    . . . . . x . . x x . . . x . . . x x . . x . . . . .
    . . . . x . . x . . x . . . x . x . . x . . x . . . .
    . . . . x . . x . . . x . . . x . . . x . . x . . . .
    . . . . x . . . x x x . x . . . x x x . . . x . . . .
    . . . . x . . . . . . . . x . . . . . . . . x . . . .
    . . . . x . . . . . . x x . x x . . . . . . x . . . .
    . . . . x x x x x x x . . . . . x x x x x x x . . . .
HERE
    
    ascii_output_1.gsub!(/^\s+/, '')
    panel = KnotworkPanel.new(2, 1)
    real_output = panel.to_aa.split("\n")
    ascii_output_1.split("\n").each_with_index do |line, i|
      assert_equal(line, real_output[i],
                   "line #{i} doesn't match")
    end
  end
  
end
   
panel = KnotworkPanel.new(8, 18)
panel.to_image()
```

Thanks to all the work we did building Tiles and Grids and ASCII art 
KnotworkPanels, we only need to add a few lines to allow KnotworkPanels to 
create a nice black and white PNG image file. Here's what we get:

![10x20 panel](/img/2004/panel.png)

Cool, eh?

## Building KnotworkPanels of Any Size

Now the program does what I want it to. But if I hand this script off to 
somebody else and say "This program will make knotwork panels of any size," 
one of their first questions will be how to set the size. "Go in and edit the 
code" won't cut it. Let's haul out our trusty 
[OptParse](http://www.ruby-doc.org/stdlib/libdoc/optparse/rdoc/classes/OptionParser.html) 
library again.

``` ruby
require 'RMagick'
require 'optparse'
  
include Magick
  
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize(str = nil)
    @pixels = []
    (0..8).each { 
      row = []
      (0..8).each { row << nil }
      @pixels << row
    }
    
    if str then
      set_from_string(str)
    end
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|" 
      }
      str += "\n"
    }
    return str
  end
end
  
# I am an arranged collection of Tiles. I know how to add and remove
# Tiles along a 2-d grid, and can also present myself as if I were a single
# large Tile.
class Grid
  def initialize(rows, columns)
    @tile_size = 9
    @rows      = rows
    @columns   = columns
    @pixels    = Array.new(rows*@tile_size) { |i|
      Array.new(columns*@tile_size)
    }
  end
  
  def set_tile(row, column, tile)
    if row >= @rows or column >= @columns then
      raise ArgumentError, \
      "set_tile at #{row}, #{column} outside of Grid area " \
      "(#{@rows}, #{@columns})"
    end
    
    pixel_origin_x = row * @tile_size
    pixel_origin_y = column * @tile_size
    (0...@tile_size).each { |tile_x|
      x = pixel_origin_x + tile_x
      (0...@tile_size).each { |tile_y|
        y = pixel_origin_y + tile_y
        @pixels[x][y] = tile.at(tile_x, tile_y)
      }
    }
  end
  
  def at(row, column)
    return @pixels[row][column]
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += row.join(' ')
      str += "\n"
    }
    
    return str
  end
  
end
  
# I am a lovely Celtic knotwork panel. I know my dimensions, and can output 
# myself as ASCII art.
class KnotworkPanel
    @@top_left = Tile.new(%{. . . . x x x x x
                            . . . . x . . . .
                            . . . . x . . . .
                            . . . . x . . . x
                            . . . . x . . x .
                            . . . . x . . x .
                            . . . . . x . . x
                            . . . . . x . . x
                            . . . . . . x x .}.gsub(/^\s+/, ''))
  
  @@top      = Tile.new(%{x x . . . . . x x
                          . . x x . x x . .
                          . . . . x . . . .
                          x x . . . x . x x
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . . x
                          . . x . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@topright = Tile.new(%{x x x x x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x . . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@left     = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@center   = Tile.new(%{. . x . . . x . .
                          . x . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . x .
                          . . x . . . x . .}.gsub(/^\s+/, '')
                        )
  
  @@right    = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@bot_left = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . x . . . x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x x x x x}.gsub(/^\s+/, '')
                        )
  
  @@bottom   = Tile.new(%{. x x . . . x . .
                          x . . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          x x . x . . . x x
                          . . . . x . . . .
                          . . x x . x x . .
                          x x . . . . . x x}.gsub(/^\s+/, '')
                        )
  
  @@botright = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x x x x x . . . .}.gsub(/^\s+/, '')
                        )
  
  def initialize(rows, columns=rows)
    @row_size = rows + 2
    @col_size = columns + 2
    
    @grid = Grid.new(@row_size, @col_size)
    
    # Set the top row
    @grid.set_tile(0, 0, @@top_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(0, i, @@top)
    end
    @grid.set_tile(0, @col_size-1, @@topright)
    
    # Set the center rows.
    (1...@row_size-1).each do |i|
      @grid.set_tile(i, 0, @@left)
      (1...@col_size-1).each do |j|
        @grid.set_tile(i, j, @@center)
      end
      @grid.set_tile(i, @col_size-1, @@right)
    end
    
    # Set the bottom row
    @grid.set_tile(@row_size-1, 0, @@bot_left)
    (1...@col_size-1).each do |i|
      @grid.set_tile(@row_size-1, i, @@bottom)
    end
    @grid.set_tile(@row_size-1, @col_size-1, @@botright)
  end
  
  def to_aa()
    return @grid.to_s
  end
  
  def to_image()
    
    filename = "panel-#{@row_size}x#{@col_size}.png"
    
    max_x = 9 * @row_size
    max_y = 9 * @col_size
    
    image = Image.new(max_x, max_y) { self.background_color = "white" }
    (0...max_y).each do |y|
      (0...max_x).each do |x|
        pixel = @grid.at(x, y)
        if pixel == "x" then
          image.pixel_color(x, y, "black")
        end
      end
    end
    image.write(filename)
    
  end
  
end
  
rows = 1
columns = 1
  
opts = OptionParser.new do |opts|
  opts.banner = "Usage #{$0} |opts|"
  opts.separator ""
  opts.separator "Specific Options"
  
  opts.on("-r", "--rows [ROWS]",
          "Number of rows for this panel (default 1)") do |r|
    rows = r.to_i
    columns = rows
  end
  
  opts.on("-c", "--columns [COLUMNS]",
          "Number of columns for this panel (default ROWS)") do |c|
    columns = c.to_i
  end
  
  opts.on_tail("-h", "--help",
               "Show this message") do
    puts opts
    exit
  end
end
  
opts.parse!
  
panel = KnotworkPanel.new(rows, columns)
panel.to_image()
```

Running it with the default should result in a 3x3 panel:

    $ ruby knotworkpanel.rb 

![3x3 panel](/img/2004/panel-3x3.png)

Setting `rows` to 2 results in a 4x4 panel.

    $ ruby knotworkpanel.rb --rows 2

![4x4 panel](/img/2004/panel-4x4.png)

<aside markdown="1">
Me from the future says "See? This is what I was talking about. You say '2 
rows', and you get a 4x4 square?  How do you think people are going to 
react? Man, I need more coffee."
</aside>

Ignoring me from the future for today, let's see what happens when we try to 
make a nice *big* KnotworkPanel.

    $ ruby knotworkpanel.rb --rows 98 --columns 73

[the results]: {{ "/img/2004/panel-100x75.png" | prepend: site.base_url }}

Hmm ... took a few seconds this time. If I cared about performance, I might go 
in and see where this could be tightened up. I don't care about performance 
today, though. I care about results. And [the results][] aren't too bad.

## Cleaning Up

Okay, it's done! That is to say, it does all the things I want it to for now.  
There's a *lot* more stuff that I would like to do with this program, but 
it's important to know when to stop and take a breath. Let's just go back and 
clean up the code a little bit. Not actually change any functionality or user 
interface, so Me From The Future is just going to have to wait. I only want 
to make it easier to read the code that I have already written.

``` ruby
require 'RMagick'
require 'optparse'
  
include Magick
  
TILE_SIZE = 9
  
# I am a single small section of a knotwork image. I know about my 
# dimensions, and can describe myself on a pixel-by-pixel basis.
class Tile
  
  def initialize(str = nil)
    @pixels = []
    1.upto(TILE_SIZE) { 
      row = []
      1.upto(TILE_SIZE) { row << nil }
      @pixels << row
    }
    
    if str then
      set_from_string(str)
    end
  end
  
  def at(x, y)
    return @pixels[x][y]
  end
  alias is_set? at
  
  def set(x, y, value=true)
    @pixels[x][y] = value
  end
  
  def unset(x, y)
    @pixels[x][y] = nil
    
    return true
  end
  
  def set_from_string(str)
    str.split("\n").each_with_index do |line, row|
      line.split(' ').each_with_index do |pixel, col|
        set(row, col, pixel)
      end
    end
  end
  
  def to_s
    str = "" 
    @pixels.each { |row|
      str += "|"
      row.each { |pixel| 
        pixel ||= " "
        str += "#{pixel}|"
      }
      str += "\n"
    }
    return str
  end
end
  
# I am an arranged collection of Tiles. I know how to add and remove
# Tiles along a 2-d grid, and can also present myself as if I were a single
# large Tile.
class Grid
  
  attr_reader :rows, :columns
  
  def initialize(rows, columns)
    @tile_size = TILE_SIZE
    @rows      = rows
    @columns   = columns
    @pixels    = Array.new(rows*@tile_size) { |i|
      Array.new(columns*@tile_size)
    }
  end
  
  def set_tile(row, column, tile)
    if row >= @rows or column >= @columns then
      raise ArgumentError, \
      "set_tile at #{row}, #{column} outside of Grid area " \
      "(#{@rows}, #{@columns})"
    end
    
    pixel_origin_x = row * @tile_size
    pixel_origin_y = column * @tile_size
    (0...&#064;tile_size).each { |tile_x|
      x = pixel_origin_x + tile_x
      (0...&#064;tile_size).each { |tile_y|
        y = pixel_origin_y + tile_y
        @pixels[x][y] = tile.at(tile_x, tile_y)
      }
    }
  end
  
  def at(row, column)
    return @pixels[row][column]
  end
  
  def to_s
    str = ""
    @pixels.each { |row|
      str += row.join(' ')
      str += "\n"
    }
    
    return str
  end
  
end
  
# I am a lovely Celtic knotwork panel. I know my dimensions, and can output 
# myself as ASCII art.
class KnotworkPanel
    @@top_left = Tile.new(%{. . . . x x x x x
                            . . . . x . . . .
                            . . . . x . . . .
                            . . . . x . . . x
                            . . . . x . . x .
                            . . . . x . . x .
                            . . . . . x . . x
                            . . . . . x . . x
                            . . . . . . x x .}.gsub(/^\s+/, ''))
  
  @@top      = Tile.new(%{x x . . . . . x x
                          . . x x . x x . .
                          . . . . x . . . .
                          x x . . . x . x x
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . . x
                          . . x . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@topright = Tile.new(%{x x x x x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x . . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@left     = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . .
                          . . . . x . . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . . x . . x
                          . . . . . x . . x
                          . . . . . . x x .}.gsub(/^\s+/, '')
                        )
  
  @@center   = Tile.new(%{. . x . . . x . .
                          . x . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          . x . x . . . x .
                          x . . . x . . . x
                          . . . x . x . x .
                          . . x . . . x . .}.gsub(/^\s+/, '')
                        )
  
  @@right    = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . x . . . . .
                          . . . x . . . . .
                          . . x . . . . . .}.gsub(/^\s+/, '')
                        )
  
  @@bot_left = Tile.new(%{. . . . . . x . .
                          . . . . . x . . .
                          . . . . . x . . x
                          . . . . x . . x .
                          . . . . x . . x .
                          . . . . x . . . x
                          . . . . x . . . .
                          . . . . x . . . .
                          . . . . x x x x x}.gsub(/^\s+/, '')
                        )
  
  @@bottom   = Tile.new(%{. x x . . . x . .
                          x . . x . x . . .
                          x . . . x . . . x
                          . x . . . x . x .
                          . . x . . . x . .
                          x x . x . . . x x
                          . . . . x . . . .
                          . . x x . x x . .
                          x x . . . . . x x}.gsub(/^\s+/, '')
                        )
  
  @@botright = Tile.new(%{. x x . . . . . .
                          x . . x . . . . .
                          x . . x . . . . .
                          . x . . x . . . .
                          . x . . x . . . .
                          x . . . x . . . .
                          . . . . x . . . .
                          . . . . x . . . .
                          x x x x x . . . .}.gsub(/^\s+/, '')
                        )  
  
  def initialize(rows, columns=rows)
    # Make room for the border tiles
    row_size = rows + 2
    col_size = columns + 2
    last_row = row_size - 1
    last_col = col_size - 1
    
    @grid = Grid.new(row_size, col_size)
    
    # Set the top row
    @grid.set_tile(0, 0, @@top_left)
    (1...last_col).each do |i|
      @grid.set_tile(0, i, @@top)
    end
    @grid.set_tile(0, last_col, @@topright)
    
    # Set the center rows.
    (1...last_row).each do |i|
      @grid.set_tile(i, 0, @@left)
      (1...last_col).each do |j|
        @grid.set_tile(i, j, @@center)
      end
      @grid.set_tile(i, last_col, @@right)
    end
    
    # Set the bottom row
    @grid.set_tile(last_row, 0, @@bot_left)
    (1...last_col).each do |i|
      @grid.set_tile(last_row, i, @@bottom)
    end
    @grid.set_tile(last_row, last_col, @@botright)
  end
  
  def to_aa()
    return @grid.to_s
  end
  
  def to_image()
    
    filename = "panel-#{@grid.rows}x#{@grid.columns}.png"
    
    x_size = TILE_SIZE * @grid.rows
    y_size = TILE_SIZE * @grid.columns
    
    image = Image.new(x_size, y_size) { self.background_color = "white" }
    (0...y_size).each do |y|
      (0...x_size).each do |x|
        pixel = @grid.at(x, y)
        if pixel == 'x' then
          image.pixel_color(x, y, 'black')
        end
      end
    end
    image.write(filename)
    
  end
  
end
  
def main
  rows    = 1
  columns = 1
  
  opts = OptionParser.new do |opts|
    opts.banner  = "Usage #{$0} |opts|"
    opts.separator ''
    opts.separator 'Specific Options'
    
    opts.on('-r', '--rows [ROWS]',
            'Number of rows for this panel (default 1)') do |r|
      rows = r.to_i
      columns = rows
    end
    
    opts.on('-c', '--columns [COLUMNS]',
            'Number of columns for this panel (default ROWS)') do |c|
      columns = c.to_i
    end
    
    opts.on_tail('-h', '--help',
                 'Show this message') do
      puts opts
      exit
    end
  end
  
  opts.parse!
  
  panel = KnotworkPanel.new(rows, columns)
  panel.to_image()
end
  
main()
```


## Conclusion

Okay, so that's about it. We've gone from an idea to a program that creates 
png formatted images of Celtic-style knotwork panels. Not bad at all. There 
are a lot of other things we could do with this program, though.

Here are a few ideas:

+ Come up with some good ideas for unit testing the image generation 
  code. Then send them to me :-)
+ Antialias the lines for a smoother effect.
+ Add color.
+ Incorporate the rest of the patterns detailed in the Andy Sloss book.
+ Add the ability to make complex panels.
+ Add the ability to scale pattern panels to any size.
+ Make Me From The Future happy by fine-tuning the KnotworkPanel 
  initializer and/or the OptParse options so that the user gets a 3x3 
  panel when they request a 3x3 panel. Oh, but what happens when the 
  user requests a 1x1 panel? I guess you'll have to figure that out.
+ Done already? Andy Sloss also wrote a book using similar techniques 
  for drawing key patterns. Go write that program, and merge it with 
  this one for a lean, mean, Celtic-art producing machine.


