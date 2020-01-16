---
aliases:
- /coolnamehere/2002/06/02_loop.html
- /post/2002/loop/
categories:
- coolnamehere
date: 2002-06-02T00:00:00Z
tags:
- pagetemplate
title: PageTemplate - Loop
type: post
updated: 2009-07-11T00:00:00Z
year: '2002'
---
<!--more-->

## Loop Basics

The `loop` directive is the most complex, and requires more explanation of its 
details. Let's start by just looking at the basic syntax of a loop in PageTemplate.

### Loop

Use the `loop` directive when you want PageTempate to insert the same chunk 
repeatedly for a list of items. It can grab values from the item to be inserted 
in `value` directives within the chunk. If there is no list of items, the `in`
chunk is skipped.

#### Syntax

<pre>
[%loop <em>list</em> %]
  Value: [%var value %]
[%end loop %]
</pre>

##### Alternate "in" syntax

Way back when, `loop` started as `in`. It seemed like the natural way of 
looking at each item in a list back in the misty days of 2002. However, the 
steadily increasing power of `in` combined with a few suggestions led to the 
addition of `loop` as a directive for loops. Makes sense. I even use it myself 
most of the time. Still, I hate it when documented features disappear without 
warning, so `in` was never removed. Here's what `in` looks like.

<pre>
[%in <em>list</em> %]
  Value: [%var value %]
[%end in %]
</pre>

`in` and `loop` both describe the same directive, so there is no difference 
in usage beyond a couple characters' worth of typing.

#### Example

    #!html
    <ul>
    [%loop books %]
      <li>"[%var title %]" by [%var author %]</li>
    [%end loop %]
    </ul>

### "Local" Values

PageTemplate works a little magic with `value` directives when stepping 
through a `loop`. First it examines the list item to see if it has a value 
for the variable named. If it can't find one there, it checks its main 
variable listing and tries to insert that. If it can't find a value in the 
main variable listing, it inserts nothing for that `value` directive.

This logic works for nested lists, too. If you have a `loop` directive 
embedded in another `loop` directive - say, a list of books written by 
each one of a list of your favorite authors - PageTemplate first looks in the 
innermost list (the books) for a name, then the next list out (the authors), 
and finally the main variable listing.

### Empty

[`if` blocks]: /post/2002/if-else-and-elsif/

Similar to the `else` directive for [`if` blocks][],
the `empty` directive provides a block of content to display if the list you 
are looking at is empty.

#### Syntax

<pre>
[%loop <em>list</em> %]
  handle list items
[%empty%]
  handle empty list
[%end loop %]
</pre>

#### Example

    #!html
    <ul>
    [%loop books %]
      <li>"[%var title %]" by [%var author %]</li>
    [%empty %]
      <li>There are no books to display</li>
    [%end loop %]
    </ul>

##### Alternate "No" Syntax

This is another idea that seemed good at the time. Back when all you had for 
loops was the `in` directive, we used `no` as the directive for empty loops. 
It's still available, but I highly discourage using it. `no` just isn't as 
clear in its intent as `empty`. But hey, I'm not going to stop you if that's 
what you really want to do.

<pre>
[%in <em>list</em> %]
  Handle list item
[%no %]
  Handle empty list
[%end in %]
</pre>

## Iterators

You are normally dealing with a hidden unnamed "this step" variable in loops. 
Most of the time this is no problem, but sometimes your template would be 
clearer if you could just hand a name to that hidden variable and access its 
traits instead of letting your value directives fling wildly off into space. 
Maybe you want to access a global value that has the same name as a loop 
value. Iterators provide you with a main spot to access loop values without 
interfering with your ability to access global values.

### Basic Iterators

Basic iterators provide an explicit name for your loop variable.

#### Syntax

<pre>
[%loop list <em>iterator</em> %]
... [%var <em>iterator.trait</em> %]
[%end loop %]
</pre>

#### Example

    #!html
    <ul>
    [%loop books book %]
      <li>"[%var book.title %]" by [%var book.author %]</li>
    [%empty %]
      <li>No books to list</li>
    [%end loop%]
    </ul>

### Multiple Iterators

It's usually easy enough to handle loops. You just step through and use the 
variable names you've been given by the programmer. It's not always that 
easy. Sometimes you get complex lists with no convenient names attached to 
them. For example, maybe you don't get a list of books with convenient labels 
for title and author. Maybe each item in your list is *another* list where the 
first item is a title and the second item is the author's name. Hey, don't 
blame me. I didn't write that code. 

Multiple iterators provide a way for you to make sense out of a confusing 
situation like that.

#### Syntax

<pre>
[%loop list <em>iterator_1 iterator_2 ... iterator_n</em> %]
  Handle list items
[%end loop %]
</pre>

#### Example

    #!html
    <ul>
    [%loop books title author %]
      <li>"[%var title]" by [%var author%]</li>
    [%empty %]
      <li>No books to list</li>
    [%end loop%]
    </ul>

## Metavariables

Metavariables are a really snazzy addition to `loop` which make formatting 
and organizing list displays much easier, without any work by you or the 
programmers.

### `__FIRST__`

True if you are on the first trip through the loop.

#### Example

    #!html
    <table class="booklist">
    [%loop books title author%]
    [%if __FIRST__ %]
      <tr>
        <th>Title</th>
        <th>Author</th>
      </tr>
    [%end if %]
      <tr>
        <td>[%var title %]</td>
        <td>[%var author %]</td>
      </tr>
    [%empty%]
      <tr>
        <td>There are no books in the list</td>
      </tr>
    [%end loop%]
    </table>
    </pre>

### `__LAST__`

True if you are on the last trip through the loop.

#### Example

    #!html
    [%loop books title author%]
    [%if __FIRST__ %]
    <table class="booklist">
      <tr>
        <th>Title</th>
        <th>Author</th>
      </tr>
    [%end if %]
      <tr>
        <td>[%var title %]</td>
        <td>[%var author %]</td>
      </tr>
    [%if __LAST__ %]
    </table>
    [%end if %]
    [%empty%]
    <p>There are no books in the list.</p>
    [%end loop%]
    </pre>

### `__ODD__`

True if you are on an odd-numbered trip through the loop (the first trip is odd).

#### Example

    #!html
    [%loop books title author%]
    [%if __FIRST__ %]
    <table class="booklist">
      <tr>
        <th>Title</th>
        <th>Author</th>
      </tr>
    [%end if %]
    [%if __ODD__ %]
      <tr class="odd">
    [%else%]
      <tr class="even">
    [%end if %]
        <td>[%var title %]</td>
        <td>[%var author %]</td>
      </tr>
    [%if __LAST__ %]
    </table>
    [%end if %]
    [%empty%]
    <p>There are no books in the list.</p>
    [%end loop%]

### `__INDEX__`

Counts the number of trips you've made through the loop (starts at zero).

#### Example

    #!html
    [%loop books title author%]
    [%if __FIRST__ %]
    <table class="booklist">
      <tr>
        <th>View</th>
        <th>Title</th>
        <th>Author</th>
      </tr>
    [%end if %]
    [%if __ODD__ %]
      <tr class="odd">
    [%else%]
      <tr class="even">
    [%end if %]
        <td><a href="/books/view/[%var __INDEX__ %]">View</a></td>
        <td>[%var title %]</td>
        <td>[%var author %]</td>
      </tr>
    [%if __LAST__ %]
    </table>
    [%end if %]
    [%empty%]
    <p>There are no books in the list.</p>
    [%end loop%]


#### Lists and WYSIWYG Editors

Here's a specific problem that might pop up when you are using a 
<acronym title="What You See Is What You Get">WYSIWYG</acronym> editor. Let's 
say you're embedding a list into a table, so that each item in the list gets 
one table row. Dreamweaver is probably not going to enjoy code like this:

    #!html
    [%loop books title author%]
    [%if __FIRST__ %]
    <table class="booklist">
      <tr>
        <th>View</th>
        <th>Title</th>
        <th>Author</th>
      </tr>
    [%end if %]
    [%if __ODD__ %]
      <tr class="odd">
    [%else%]
      <tr class="even">
    [%end if %]
        <td><a href="/books/view/[%var __INDEX__ %]">View</a></td>
        <td>[%var title %]</td>
        <td>[%var author %]</td>
      </tr>
    [%if __LAST__ %]
    </table>
    [%end if %]
    [%empty%]
    <p>There are no books in the list.</p>
    [%end loop%]

The problem is that the `end`, `else`, and `if` directives are at invalid 
locations for XHTML, and they may not be allowed by your editor.

It turns out that the solution is simple, though maybe a little awkward. 
Wrap the offending directives in HTML comments, like this example shows:

    #!html
    <!-- [%loop books title author%] -->
    <!-- [%if __FIRST__ %] -->
    <table class="booklist">
      <tr>
        <th>View</th>
        <th>Title</th>
        <th>Author</th>
      </tr>
    <!-- [%end if %] -->
    <!-- [%if __ODD__ %] -->
      <tr class="odd">
    <!-- [%else%] -->
      <tr class="even">
    <!-- [%end if %] -->
        <td><a href="/books/view/<!-- [%var __INDEX__ %] -->">View</a></td>
        <td><!-- [%var title %] --></td>
        <td><!-- [%var author %] --></td>
      </tr>
    <!-- [%if __LAST__ %] -->
    </table>
    <!-- [%end if %] -->
    <!-- [%empty%] -->
    <p>There are no books in the list.</p>
    <!-- [%end loop%] -->

Your fancy editor should be able to handle this, and PageTemplate should be 
able to understand it just fine. The only side effect is that you will have 
some empty comments in your final page.

[Vim]: {% tag_link vim %}
[Emacs]: {{ "/emacs" | prepend: site.base_url }}

The other solution is to use [Vim][], [Emacs][],
or some other effective non-<acronym title="What You See Is What You Get">WYSIWYG</acronym> editor. 
Personal preference, of course. I know that Dreamweaver costs good money, and 
you aren't going to toss it aside just because I say so.  Hopefully this 
workaround will suit your needs.

