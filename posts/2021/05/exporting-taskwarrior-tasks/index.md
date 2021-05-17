---
title: exporting taskwarrior tasks
slug: exporting-taskwarrior-tasks
description: In which I get real weird with Taskwarrior and Hugo
caption:
draft: true
tags:
- taskwarrior
- hugo
- tools
date: 2021-05-17
---
I keep trying to add this stuff into other posts.
It deserves its own post.

{{< console >}}
$ task export status:pending -work -pay -finances -personal '(priority:H or priority:M)'
{{< /console >}}

{{< note >}}
`task export` ignores normal concerns like context or task status, so I need to apply those myself.
{{</ note >}}

This produces an array of JSON objects, something like this:

``` json
[
  ⋮
  {
    "id": 173,
    "description": "data tables in hugo",
    "due": "20200605T065959Z",
    "entry": "20200604T193414Z",
    "modified": "20200604T193435Z",
    "priority": "H",
    "project": "Site",
    "status": "pending",
    "tags": ["blog"],
    "uuid": "8d7117d9-2faf-4a98-bf4b-e88a3d44ccd1",
    "urgency": 16.472
  }
]
```

{{< console >}}
$ task export status:pending -work -pay -finances -personal '(priority:H or priority:M)' \
  | in2csv -f json \
  | csvcut -c id,description,priority,project,urgency,tags/0,tags/1 \
  | csvsort -rc urgency \
  | head -n 5
{{< /console >}}

{{< csv-table caption="Most urgent tasks, CSV version" header=true >}}
id,description,priority,project,urgency,tags/0,tags/1
173,data tables in hugo,H,Site,16.4091,blog,
167,promote script should check adoc,H,Site,7.90411,ops,
34,redo Voodoo Vince for dbh,M,Artbiz,7.8,art,inventory
17,store link on every page,M,Site,7.7,layout,
{{< /csv-table >}}

okay now do json tables

okay now do a shortcode to emulate a taskwarrior report