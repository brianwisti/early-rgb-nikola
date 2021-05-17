---
slug: taskwarrior-contexts
date: 2018-02-04 00:00:00+00:00
draft: false
series:
- Taskwarrior Babysteps
tags:
- taskwarrior
- tools
title: Taskwarrior Contexts
uuid: 8a6d9e9a-eba8-49ac-94b1-37da66b5ec56
aliases:
- /2018/02/04/taskwarrior-contexts/
---
I manually applied tag filters to keep task listings relevent in my
previous Taskwarrior [posts](/tags/taskwarrior), but
[Taskwarrior](https://taskwarrior.org/) provides
[contexts](https://taskwarrior.org/docs/context.html) to apply filters
automatically. Let’s use those instead.

## What is a context?

Taskwarrior contexts are predefined filters appropriate to a particular
set of circumstances. Once you define and load your context, Taskwarrior
automatically applies the context’s filter for reporting. You can use
them to focus on tasks important to those circumstances: work, craft
projects, unsorted ideas, or home projects.

I removed sensitive tasks from `task` output with manual filters like
`-work`. A special context for my blog would let me concentrate on
writing instead of remembering that filter every time.

## Using contexts

To create a context, use `context define` with its name and filter
rules.

{{< console >}}
$ task context define blog -work
Are you sure you want to add 'context.blog' with a value of '-work'? (yes/no) yes
Context 'blog' defined. Use 'task context blog' to activate.
{{< /console >}}

Now I have a context that includes everything but `+work` tasks.
Perfect.

Maybe another context for *only* work tasks?

{{< console >}}
$ task context define work +work
{{< /console >}}

How do I get a handy list of created contexts?

{{< console >}}
$ task context list

Name Definition Active
blog -work      no
work +work      no
{{< /console >}}

I could get carried away with new contexts, but I’ll keep it to three
for now: at work, on the blog, and *everywhere* — no context at all. I
can add more later.

Before I start using the contexts, how many tasks do I have?

{{< console >}}
$ task count
153
{{< /console >}}

[`count`](https://taskwarrior.org/docs/commands/count.html) counts every
task, including those that I completed or deleted. Let’s apply the
`+PENDING` [virtual
tag](https://taskwarrior.org/docs/tags.html#supported) to only count
incomplete tasks.

{{< console >}}
$ task +PENDING count
63
{{< /console >}}

With these numbers in my head, let’s set the “blog” context.

{{< console >}}
$ task context blog
Context 'blog' set. Use 'task context none' to remove.
{{< /console >}}

Now how many tasks do I have?

{{< console >}}
$ task count
112
$ task +PENDING count
53
{{< /console >}}

Okay, I don’t have that many `+work` tags. It’s still nice not to worry
about them when writing.

How do I see what context I am in? `context list` includes a column to
show the active context.

{{< console >}}
$ task context list

Name Definition Active
blog -work      yes
work +work      no
{{< /console >}}

However, it might be clearer to show only the current context.

{{< console >}}
$ task context show
Context 'blog' with filter '-work' is currently applied.
{{< /console >}}

Context affects reporting, but does not affect task creation. I can
create a `+work` task from my "blog" context. It just won’t show up in
any reports until I switch context.

Taskwarrior maintains context across shell sessions, so eventually I
will want to clear the current context.

{{< console >}}
$ task context none
{{< /console >}}

I must confess something, dear reader. This post has been sitting as a
draft for almost a month. My Taskwarrior usage evolved during that
month. I create fewer `+work` tasks, because it often duplicated effort
between Taskwarrior and the issue tracker used at work. I still have a
few for side tasks that don’t fit neatly into work’s ticketing system. I
don’t really have enough to merit a work context, though.

I may as well delete the “work” context.

{{< console >}}
$ task context delete work
Are you sure you want to remove 'context.work'? (yes/no) yes
Context 'work' deleted.
$ task context list

Name   Definition      Active
blog   -work           yes
bucket +idea -PRIORITY no
{{< /console >}}

Oh yeah — the bucket. That’s new since I started this post.

I get a lot of ideas. Some of them are awful. Some of them seem worth
doing. They all go in Taskwarrior. Every once in a while I sit down with
a cup of coffee and sort through unexamined ideas: tasks tagged `+idea`
and without an assigned priority. That’s what the “bucket” context is
there for.

The interesting ideas get a priority — usually `L` unless they excite
me. The uninteresting ones get deleted.

That’s all for now. Have fun getting something done\!