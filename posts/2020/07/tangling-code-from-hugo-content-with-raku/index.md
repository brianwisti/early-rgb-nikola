---
caption: You know what else I can tangle? Yarn!
date: 2020-07-08 21:45:00-07:00
updated: 2020-09-03 09:29:00-07:00
description: I could just use Org mode, but noo that's too easy
draft: false
slug: tangling-code-from-hugo-content-with-raku
tags:
- RakuLang
- LiterateProgramming
- Files
- Hugo
- SortOf
- programming
title: Tangling code from Hugo content with Raku
previewimage: /images/2020/07/tangling-code-from-hugo-content-with-raku/cover.jpg
---
{{< aside title="Updates" >}}
[codesections]: https://fosstodon.org/@codesections

2020-09-03
: [codesections][] found a typo! I forgot to *show* the target file name once command line arguments
  are in place. It should go `raku tangle-fragments.raku index.md`.
{{< /aside >}}
Let's say I have a file.
The one you're reading, perhaps.
Well, its original Markdown content.

It has a shortcode in it.

``` go-html-template
{{</* code file="hello.py" */>}}
print("Hello")
{{</* /code */>}}
```

[hugo docs]: https://github.com/gohugoio/hugoDocs/blob/master/layouts/shortcodes/code.html

I based `{{</* code */>}}` here on a shortcode from the [hugo docs]. It presents highlighted code with additional context.

{{< code file="hello.py" >}}
print("Hello")
{{< /code >}}

Really handy when you're writing about code.  Thing is, now I have two copies.  There's one here in
the shortcode, and another in a `hello.py` file that I'm writing about.  I'd prefer there was only a
single copy.  That way they don't get out of sync.

[`readFile`]: https://gohugo.io/functions/readfile/

I *could* use Hugo's [`readFile`] function in a new shortcode, including the contents of
`hello.py` in this Markdown file. Something like this:

``` go-html-template
{{</* include file="hello.py" */>}}
```

{{< aside >}}
Actual shortcode logic left as an exercise for the reader.
{{</ aside >}}

[Org mode]: /tags/org-mode

But that still breaks up the writing flow a little bit. I'm writing the code over here, and
writing *about* it over there. It's a tiny complaint, but working with [Org mode] has spoiled me. I
get to write the code in the same document that I'm writing about it in. Everything stays in sync,
more or less.

What I want is to write about `hello.py` here, and with a command have `hello.py` appear on my
filesystem, containing the Python code I've been describing.

And I want to do it without disturbing Hugo. Let it turn Markdown into HTML.

## Tangling

[Literate Programming]: http://literateprogramming.com/index.html
[noweb]: https://www.cs.tufts.edu/~nr/noweb/
[Babel]: https://orgmode.org/worg/org-contrib/babel/intro.html

This process is called "tangling," and it's popular in the admittedly small world of [Literate
Programming]. The code is interleaved throughout some kind of document, and a tool like [noweb] or
[Babel] parses the document to create code files. Could be any kind of file, really. The process can get
fancy.

But the start is not fancy: given a text file containing a `{{</* code file="(something)" */>}}`,
write the contents of that shortcode to the named file.

{{< code file="tangle.raku" >}}
sub MAIN() {
  my $filename = "index.md";
  my $opener = '{{</* ';
  my $closer = ' */>}}';
  my regex shortcode {
    $opener
      code \s
      'file="' $<filename> = .+? '"'  # Remember the filename
      .*?
    $closer
    \n                # Ignore leading newline
    $<content> = .+?  # Remember everything else in the block
    \n                # Ignore leading newline
    $opener '/code' $closer
  }

  my $markdown = slurp $filename;

  if $markdown.match(/ <shortcode> /) {
    my $tangle-file = $/<shortcode><filename>;
    my $tangle-content = $/<shortcode><content>;
    spurt $tangle-file, $tangle-content;
    say "Tangled to $tangle-file";
  }
}
{{< /code >}}

[regular expressions]: https://docs.raku.org/language/regexes
[grammar]: https://docs.raku.org/language/grammars

I love Raku's approach to [regular expressions].  For starters, the syntax looks a bit more like
describing a grammar.  I can break the funny regex characters up with spaces, and clarify them with
comments.  In fact, I could someday build this up to a real [grammar].

Secondly, it addresses the fact that most text we look at these days contains multiple lines.
I didn't have to worry about any special multiline flags to get this working.

[Hash]: https://docs.raku.org/language/hashmap

Finally, getting at the named captures was — I wouldn't say "obvious," but at least "coherent."
I can treat the match variable `$/` as a nested [Hash].
The important bits look something like this:

```
shortcode =>
  filename => ｢hello.py｣
  content => ｢print("Hello")｣
```

I can grab the named capture `filename` of my matched `shortcode` regex with
`$/<shortcode><filename>` — or `~$<shortcode><filename>`, depending on your preferred syntax.

[REBOL]: /tags/rebol

This is all possible in languages like Perl with assorted flags, but I haven't seen parsing treated
so well by default since maybe [REBOL].

Anyways, let's run this thing.

{{< console >}}
$ raku tangle.raku
Tangled to hello.py
$ bat hello.py
───────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: hello.py
───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ print("Hello")
───────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────
{{< /console >}}

Sweet.

Except — this Markdown file I'm writing.
It has *two* file code blocks now.
I want to tangle both of them.

## Multiple output files

This requires a couple changes, since I'm writing code about Hugo shortcodes in a Hugo post.

To show shortcode directives without Hugo evaluating them, they need to look like shortcode
comments. Their contents will get passed straight through as part of your post.
To show `{{</* shortcode */>}}` in a post, your Hugo content needs `{{</*/* shortcode */*/>}}`.

So that's lovely and all, but can be a headache of its own for this specific situation of extracting
code from a blog post. 

I need to remember this commented shortcode syntax.

{{< code name="define-commented-shortcodes" lang="raku" >}}
  my $commented-opener = '{{' ~ '</* ';
  my $commented-closer = ' */>' ~ '}}';
{{< /code >}}

{{< aside >}}
Goodness, that looks silly. Well, I'm writing this blog post as a test case for the code.  I
couldn't figure out how to cleanly present the commented shortcode delimiters without Hugo and my
code getting into a fierce argument.

If I wasn't writing the code *in* this post, I could use something simpler, like this:

``` raku
  my $commented-opener = '{{</*/* ';
  my $commented-closer = ' */*/>}}';
```

But that's not the path I chose.
It's not easy to write programs that write themselves. Sometimes you must help them along.
{{< /aside >}}

That way I can replace those commented shortcode delimiters with their normal counterparts when I tangle later.

{{< code name="replace-commented-shortcodes" lang="raku" >}}
      my $tangle-content = $block<shortcode><content>
        .subst(:global, / $commented-opener /, $opener)
        .subst(:global, / $commented-closer /, $closer);
{{< /code >}}

Now that I have that particular detail out of the way, tangle every block? Sure! Make a regular
expression match `:global` and it returns a list containing every match. 

{{< code name="tangle-every-block" lang="raku" >}}
  my $markdown  = slurp $filename;
  my @fragments = $markdown.match(/<shortcode>/, :global);

  for @fragments -> $block {
    my $tangle-file = $block<shortcode><filename>;
    «replace-commented-shortcodes»
    spurt $tangle-file, $tangle-content;
    say "Tangled to $tangle-file";
  }
{{< /code >}}

I think that about covers it. The shortcode recognition logic can stay the same.

{{< code file="tangle-multi.raku" >}}
sub MAIN() {
  my $filename = "index.md";
  my $opener = '{{</* ';
  my $closer = ' */>}}';

  my regex shortcode {
    $opener
      code \h
      'file="' $<filename> = .+? '"'  # Remember the filename
      .*?
    $closer
    \n                # Ignore leading newline
    $<content> = .+?  # Remember everything else in the block
    \n                # Ignore trailing newline
    $opener '/code' $closer
  }

  «define-commented-shortcodes»

  «tangle-every-block»
}
{{< /code >}}

And it works!

```
$ raku tangle-multi.raku
Tangled to hello.py
Tangled to tangle.raku
$ bat tangle.raku
───────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: tangle.raku
───────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ sub MAIN() {
   2   │   my $filename = "index.md";
   3   │   my $opener = '{{</* ';
   4   │   my $closer = ' */>}}';
   5   │   my regex shortcode {
   6   │     $opener
   7   │       code \s
   8   │       'file="' $<filename> = .+? '"'  # Remember the filename
   9   │       .*?
  10   │     $closer
  11   │     \n                # Ignore leading newline
  12   │     $<content> = .+?  # Remember everything else in the block
  13   │     \n                # Ignore leading newline
  14   │     $opener '/code' $closer
  15   │   }
  16   │
  17   │   my $markdown = slurp $filename;
  18   │
  19   │   if $markdown.match(/ <shortcode> /) {
  20   │     my $tangle-file = $/<shortcode><filename>;
  21   │     my $tangle-content = $/<shortcode><content>;
  22   │     spurt $tangle-file, $tangle-content;
  23   │     say "Tangled to $tangle-file";
  24   │   }
  25   │ }
───────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

Unfortunately, I'm not quite done yet.

## Multiple fragments

I'm not done yet because I don't like to describe my code a full file at a time. I'd rather talk
about this bit here, explain that bit over there, then mash it all up in the end.

Consistency counts, so I need to pick a syntax. Well — you've been reading along. You can see that I
already made my choice.  I got used to `<<fragment-text>>` in Babel, where the attribute is called
`name`. Might as well keep doing that over here. Oh but hang on. I want it to stand out a bit. I'll
use angle quotes `«‥»`.

{{< note >}}
[Vim or Neovim]: /tags/vim
[digraph]: https://vimhelp.org/digraph.txt.html#digraph.txt
[Compose]: https://en.wikipedia.org/wiki/Compose_key

On a US keyboard using [Vim or Neovim], `«` is a [digraph] which can be entered via `Control-k` followed by `<` `<`.
Or if you've set up a [Compose] key, it's `Compose` followed by `<` `<` in any editor.

`»` is the same, but `>` `>` instead.

*Or* you can use `<<…>>` in your code and ignore my recent obsession with fancy characters.

Yes, I know I could practically write it *all* with fancy characters in Raku. One step at a time.
{{< /note >}}

Let's go back to the Python code because it's still so small.

[Rich]: https://rich.readthedocs.io/en/latest/

Say I want to demonstrate the delightful [Rich][] terminal library for Python.

{{< code name="import-libraries" lang="python" >}}
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
{{< /code >}}

But before I really use it in my code, I spend 1,500 words singing its praises.

It's nice. I like it.

Okay, done singing. Time to write the rest of the program.

{{< code file="rich-hello.py" >}}
«import-libraries»

md = Markdown("**Hello**, *World*.")
print(Panel(md))
{{< /code >}}

I identify the fragment with a `name` attribute:

``` go-html-template
{{</* code name="import-libraries" lang="python" */>}}
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
{{</* /code */>}}
```

My `code` block references the `import-libraries` fragment by name when I'm ready for it.

``` go-html-template
{{</* code file="rich-hello.py" */>}}
«import-libraries»

md = Markdown("**Hello**, *World*.")
print(Panel(md))
{{</* /code */>}}
```

{{< aside >}}
I *might* spend some time talking about the `code` shortcode in another post, but I dislike Go's
templating enough that this does not sound like fun.
{{< /aside >}}


### Rounding up fragments to tangle

Recognizing an additional parameter doesn't make my regular expression *that* much more
complicated, but I can see things getting more complex — or me finding a better pattern later — so
let's give the params their own named regex for some encapsulation.

{{< code name="shortcode-params-regex" lang="raku" >}}
  my regex params {
      'file="' $<filename> = .+? '"'
      ||
      'name="' $<fragment> = .+? '"'
  }
{{< /code >}}

That way I can drop it in `shortcode` to say "oh and look for `params` while you're at it please."

{{< code name="nested-shortcode-regex" lang="raku" >}}
  «shortcode-params-regex»
  my $opener = '{{</* ';
  my $closer = ' */>}}';

  my regex shortcode {
    $opener code \s <params> .*? $closer
    \n                # Ignore leading newline
    $<content> = .+?  # Remember everything else in the block
    \n                # Ignore trailing newline
    $opener '/code' $closer
  }
{{< /code >}}

Okay, we recognize `file` and `name` parameters. What do we do with them?
We gather them!

{{< code name="gather-fragments-and-files" lang="raku" >}}
    my %fragment-for;
    my @filenames;
    my $markdown = slurp $filename;

    for $markdown.match(/<shortcode>/, :global) -> $block {
      my $tangle-content = $block<shortcode><content>;
      my $params = $block<shortcode><params>;
      my $fragment = $params<fragment> || $params<filename>;

      if $fragment {
        say "fragment: $fragment";
        %fragment-for{ $fragment.Str } = $tangle-content;
      }

      if my $filename = $params<filename> {
        @filenames.push($filename.Str);
      }
    }
{{< /code >}}


### Tangling my fragments

Let's see here. I know before I can write any files, I need to make sure everything's tangled.
Trying to keep fragments easy to identify.
They sit on a line by themselves, possibly with some leading whitespace.

{{< code name="tangle-fragments" lang="raku" >}}
    my regex fragment { ^^ \h*? "«" $<name> = .+? "»" $$ }
    my %tangle-for;

    «tangle-function»

    for %fragment-for.keys -> $name { tangle($name); }
{{< /code >}}

{{< note >}}
[class]: https://docs.raku.org/language/classtut

Raku functions are lexically scoped, which means it's perfectly okay to declare a function inside
another function. Though next time I revisit this, I may want to think about a [class] or something to
hold the complexity.
{{< /note >}}

But what does that function need to look like? I'm still not sure I got it quite right. I mean I
know the *basic* shape of it.

{{< code name="tangle-function" lang="raku" >}}
    sub tangle(Str $name) {
      «tangle-error-checking»

      «tangle-text»
    }
{{< /code >}}

It needs some error checking. I know that much. Oh, and if it's already been tangled I should
avoid going through it again.

{{< code name="tangle-error-checking" lang="raku" >}}
      return "" unless $name;

      if %tangle-for{ $name } {
        return %tangle-for{ $name }.Str;
      }

      my $content = %fragment-for{ $name };
      unless $content {
        die "«$name» is not a valid fragment";
      }
{{< /code >}}

The idea of the thing is clear enough. Find and recursively `tangle` each fragment found in this
text, replacing the fragment references with their tangled text. Once that's all done, cache and
return the tangled text.

{{< code name="tangle-text" lang="raku" >}}
      for $content.match(/ <fragment> /, :global) -> $match {
        my $fragment-ref = $match.Str;
        my $fragment-name = $match<fragment><name>.Str;
        say "$name ← «$fragment-name»";
        $content.subst-mutate(/$fragment-ref/, tangle( $fragment-name));
      }

      %tangle-for{ $name } = $content;
{{< /code >}}

I flailed while tangling fragments.  Lots of complaints from Raku about the difference between
a `Match` and a `String`.  There *must* be better ways.  But the most important thing? I got it to
work eventually.

### Writing tangled files

After all that, writing the tangled files felt easy. 

{{< code name="write-tangled-files" lang="raku" >}}
    «define-commented-shortcodes»

    for @filenames -> $tangle-file {
      my $tangle-content = %tangle-for{ $tangle-file }
        .subst(:global, / $commented-opener /, $opener)
        .subst(:global, / $commented-closer /, $closer);
      spurt $tangle-file, $tangle-content;
      say "Tangled to $tangle-file";
    }
{{< /code >}}

Then — theoretically — all these fragments I wrote will make a useful code tangler!

Might as well make it so this script can look at more than just the file I'm editing right now.

{{< code file="tangle-fragments.raku" lang="raku" >}}
sub MAIN(Str $filename) {
  «nested-shortcode-regex»

  «gather-fragments-and-files»

  «tangle-fragments»

  «write-tangled-files»
}
{{< /code >}}

[CLI]: https://docs.raku.org/language/create-cli

Easiest [CLI] I ever wrote, by the way. See?

{{< console >}}
$ raku tangle-fragments.raku
Usage:
  tangle-fragments.raku <filename>
{{< /console >}}

Time for the real thing.
I'm nervous.
I shouldn't be nervous.
I know how this story ends.
Then again I keep rewriting the middle.

{{< console >}}
$ raku tangle-fragments.raku index.md
fragment: hello.py
fragment: tangle.raku
fragment: define-commented-shortcodes
fragment: replace-commented-shortcodes
fragment: tangle-every-block
fragment: tangle-multi.raku
fragment: import-libraries
fragment: rich-hello.py
fragment: shortcode-params-regex
fragment: nested-shortcode-regex
fragment: gather-fragments-and-files
fragment: tangle-fragments
fragment: tangle-function
fragment: tangle-error-checking
fragment: tangle-text
fragment: write-tangled-files
fragment: tangle-fragments.raku
tangle-function <-- (tangle-error-checking)
tangle-function <-- (tangle-text)
nested-shortcode-regex <-- (shortcode-params-regex)
tangle-every-block <-- (replace-commented-shortcodes)
tangle-fragments <-- (tangle-function)
write-tangled-files <-- (define-commented-shortcodes)
tangle-fragments.raku <-- (nested-shortcode-regex)
tangle-fragments.raku <-- (gather-fragments-and-files)
tangle-fragments.raku <-- (tangle-fragments)
tangle-fragments.raku <-- (write-tangled-files)
rich-hello.py <-- (import-libraries)
tangle-multi.raku <-- (define-commented-shortcodes)
tangle-multi.raku <-- (tangle-every-block)
Tangled to hello.py
Tangled to tangle.raku
Tangled to tangle-multi.raku
Tangled to rich-hello.py
Tangled to tangle-fragments.raku
{{< /console >}}

That overwrote my test version of `tangle-fragments.raku`.
Scary.
Ran the new version to keep myself honest.
It produced the same output, and appears to have correctly tangled my fragments!

{{< console >}}
$ bat rich.hello.py
───────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: rich-hello.py
───────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ from rich import print
   2   │ from rich.panel import Panel
   3   │ from rich.markdown import Markdown
   4   │
   5   │ md = Markdown("**Hello**, *World*.")
   6   │ print(Panel(md))
───────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────
{{</ console >}}

Running `rich-hello.py` looks more interesting with a screenshot than a text block:

![terminal screenshot](rich-panel.png
  "formatted output using Rich")

Okay.
*Now* I'm done.

I *could* have done this in Python.
There are decent parsing libraries out there.
But Raku did this on its own, without pulling in any extra — without pulling in *any* libraries.

## Done? You barely started!

My tangle script is no competition for Org mode's Babel.

[Chroma]: https://github.com/alecthomas/chroma

* It needs more error checking
  - circular fragment references
  - unreachable files (path, permissions)
* smart handling of whitespace and indentation, to keep Python from becoming a chore
* rendering fragment names in such a way that syntax highlighters can do something pretty with them
  (Especially when writing code in a language that [Chroma] has heard of)
* hidden blocks
* code evaluation and display of results

But it'll do for now.