---
title: Learning a little elisp
slug: learning-a-little-elisp
description: Don't get impressed yet
date: 2020-12-19 16:30:00-08:00
tags:
- elisp
- emacs
- org mode
- programming
draft: false
---
<div class="note">
  <div></div>

Excuse me while I share a sleep-deprived ramble from last night through about five lines of [Emacs Lisp](https://www.gnu.org/software/emacs/manual/html%5Fnode/eintr/index.html).

</div>

There's [tons](https://www.gnu.org/software/emacs/manual/html%5Fnode/eintr/index.html) of [detailed](https://caiorss.github.io/Emacs-Elisp-Programming/) information about Emacs LISP —
aka Emacs Lisp, elisp, ELisp, and "oh my god they love parentheses" — out there.
I just want my old "Babysteps" approach, so all the detailed sites won't be so intimidating.

Gotta do it myself, I guess.


## Why {#why}

So far I have treated elisp as an arcane configuration language.
But it's so much more than that.
It's also an arcane _programming_ language.
I do love learning programming languages.

I'll have an easier time configuring Emacs, and most likely get strange new ideas for ways to extend my frenemy text editing environment.


## How {#how}

Using [Emacs](https://www.gnu.org/software/emacs/), of course!
A little bit with the deep integration for both [evaluation](https://www.gnu.org/software/emacs/manual/html%5Fnode/emacs/Lisp-Eval.html#Lisp-Eval) and [documentation](https://www.gnu.org/software/emacs/manual/html%5Fnode/emacs/Lisp-Doc.html#Lisp-Doc) of Lisp.
Probably a bit more with [Org Babel](https://orgmode.org/worg/org-contrib/babel/intro.html), which provides a layer for evaluating code and exporting the results —
say, for example, to a blog post like this one.

Expect side notes about [Doom Emacs](https://github.com/hlissner/doom-emacs), since that's the flavor I use lately.


## Let's get started {#let-s-get-started}

I looked up "Hello World in ELisp" and found something like this.

<a id="code-snippet--elisp-hello-world"></a>
```elisp
(message "Hey World!")
```


### ELisp evaluation {#elisp-evaluation}

Want to write some Emacs Lisp?
Here you go.

-   Open Emacs.
-   Type `(message "Hey World!")`.
    Put your cursor — the _point_ — just outside the closing parenthesis.
-   Hit <kbd>C-x e</kbd>.
-   Emacs prints `Hey World!`.

Boom.
Done.

The `()` indicate an [s-expression](https://en.wikipedia.org/wiki/S-expression).
That's _symbolic expression_, or _sexpr_ if you're cool.
S-expressions aren't quite the atoms of a Lisp program.
There are smaller bits, like the symbol `message` or the value `"Hey World!"`.
But it's the smallest _useful_ element.
Oh I know.
S-expressions are the _molecules_ of a Lisp program.

No?
How about words vs sentences?
Okay, whatever.

This particular s-expression holds an _ordered pair_, `message` and `"Hey World!"`.
_Pair_ because there are two items.
_Ordered_ because the order matters.

When ELisp sees an ordered pair, it knows what to do:

-   figure out what it gets from the second thing
-   hand that to the first thing
-   hand _that_ result to you

The part that feels magic is each of the items in the pair can be s-expressions too!
Try `(sqrt (* 37 37))`.
`37.0`, right?

That `*` is for multiplication.
So we're multiplying `37` by `37` and proving to ourselves that `sqrt` hands us back `37`.
It's a bit of a pointless example, but hey welcome to me learning stuff.
And there's my first lesson:

A Lisp program is pretty much just infinitely nested s-expressions.

And macros.
Macros, near as I can tell, are infinitely nested s-expressions with gloves and a nice hat.

BTW I don't know Lisp.
I hope you did not come here expecting a tutorial.


### ELisp documentation {#elisp-documentation}

When we have a question about ELisp functions, we don't need to look everything up online.
Emacs comes with notes.

-   Put _point_ over `message` in `(message "Hey world!")`
-   Hit <kbd>C-h f</kbd>
-   See the prompt asking me to specify a function, with `message` pre-filled
-   Hit <kbd>ENTER</kbd>
-   Learn things!

<div class="note">
  <div></div>

Doom uses <kbd>SPC h f</kbd> to fetch function descriptions.
Oh hey, while you're at it try <kbd>SPC h d h</kbd> for general Doom help,
or <kbd>SPC h d m</kbd> for help with a specific mode!

</div>


### ELisp in Org Babel {#elisp-in-org-babel}

This is great and all, but I am less concerned about live evaluation of ELisp.
Org mode is more interesting to me.
I could make my [config](/config) smarter.
For example, only tangle a section if it's relevant for that machine.

And, of course, really handy for blogging about ELisp.

<div class="note">
  <div></div>

Configuration of Org and Babel is traditionally an elaborate ritual.
In Doom, it's enough for this post to enable `org`.

Somewhere in my `init.el` I have these lines.

```elisp
:lang
(org +roam +hugo)
```

Okay, I added `+hugo` since I'm using [`ox-hugo`](https://ox-hugo.scripter.co/) to integrate with my workflow.
And `+roam` beause [Org-roam](https://www.orgroam.com/) is kinda cool.
But not relevant for today.

</div>

I need a code block written in a language that Babel knows.
It should not surprise us that Babel knows ELisp.

```org
#+begin_src elisp
(message "Hey World!")
#+end_src
```

I press <kbd>C-c C-c</kbd> with _point_ over the code block.

<div class="note">
  <div></div>

Or <kbd>ENTER</kbd> in Doom.

</div>

Suddenly: a `#+RESULTS:` block!

```org
#+RESULTS:
: Hey World!
```

I can also write my ELisp inline:

```org
src_elisp{(sqrt (* 37 37))}, right?
```

Written like this, Babel replaces my code with its result when `ox-hugo` exports the post.

All right.
That's the very basics of evaluating ELisp in Emacs generally and Org mode in particular.

Let's get back to the code, please.
How do I do variables?


## Displaying a variable {#displaying-a-variable}

Let's see.
`setq` to set a variable for my name.
identifiers can be pretty much whatever.
I'll use lowercase letters and a hyphen.

Looks like `format` can smush it into a string for `message`.

<a id="code-snippet--hello-brian-setq"></a>
```elisp
(setq my-name "Brian")
(message
 (format "hello %s" my-name))
```

`format` does its work and hands the result back to `message`, which displays the result.

```text
hello Brian
```

Thing is, now `my-name` is floating around forever what with being a global variable.

<a id="code-snippet--global-my-name"></a>
```elisp
(message my-name)
```

```text
Brian
```

What if I used a local variable instead?

```elisp
(let ((new-name "Whozzomongo"))
     (message new-name))
```

```text
Whozzomongo
```

But back out here it doesn't exist.

```elisp
(new-name)
```

You don't see anything out here,
but when I tried to <kbd>C-c C-c</kbd> that, Emacs complained:

> Symbol's function definition is void: `new-name`

I consider that a good thing.
Global variables make me nervous, especially in long-running applications.

So I know how to set global or local variables.
I know how to display them.

How to get them from the user?


## Getting user input {#getting-user-input}

[Xah Lee](http://www.ergoemacs.org/emacs/elisp%5Fidioms%5Fprompting%5Finput.html) gives a nice rundown on how to get user input.
`read-string` is the one I want.

<a id="code-snippet--read-string-name"></a>
```elisp
(read-string "What's your name? ")
```

`read-string` returns whatever I answer.

```text
Waffle Smasher The Magnificent Pineapple
```

Let's make a question prompt.
The inside-out approach of nested evaluation confuses me a bit,
so I'll happily let Emacs indent things however it wants.

```elisp
(message
 (let
     ((question "What's your name?")
      (message "Go to bed, %s!"))
   (format message
           (read-string (format "%s " question)))))
```

```text
Go to bed, Dude!
```

I did some things.
`read-string` puts the cursor right after the `question` prompt.
So to help myself while I'm figuring all this out, I created some local variables.
`question` holds the question to be answered.
`message` holds the —

<div class="note">
  <div></div>

Wait, there's already a global _standard_ function called `message`!

</div>

It's cool.
By the time I need the function, `let` is done and my variable doesn't exist.
Still.
I shouldn't make this a habit.


## Wrapping it in a function {#wrapping-it-in-a-function}

I wasn't planning on looking at functions today, but I'm more than halfway there already.

```elisp
(defun ask-and-respond (question-for-user our-response)
  "Ask the user a question and show them a response."
  (interactive)
  (message
   (format our-response
           (read-string (format "%s " question-for-user)))))
```

Use the [`defun`](https://www.gnu.org/software/emacs/manual/html%5Fnode/eintr/defun.html#defun) macro to _define functions_.
It's similar enough to function definitions in other languages.

```text
(defun NAME (ARGUMENTS…)
  "A docstring"
  THE CODE)
```

Though there are some differences right off the bat.
`ask-and-respond` needs user input.
ELisp requires I mark those as [interactive](https://www.gnu.org/software/emacs/manual/html%5Fnode/eintr/Interactive.html#Interactive).

Other than _that_ it's similar enough to function definitions in other languages.

I already know how to call a function.

```elisp
(ask-and-respond "What's your name?" "Goodnight, %s!")
```

```text
Goodnight, Brian!
```

Okay, time to take my own hint.
Good night!