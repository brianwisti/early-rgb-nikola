---
title: Building reactions data from my webmentions feed
tags:
- IndieWeb
- Python
- Site
- Data
draft: true
series:
- fixing my webmentions
date: 2021-05-17
---
:LOGBOOK:

-   State "DRAFT"      from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2020-11-08 Sun 21:04]</span></span>

:LOGBOOK:

So what _didn't_ work well: making one big `mentions.json` file hold every detail about every reaction on the site.
It was hard to be sure I had the latest reactions to an individual page.
My code for the task was filled with late night cleverness.
Very difficult to untangle in the light of day.

This time around it's going straight from my feed to a SQLite database, by way of sqlite-utils.
JF2 has enough variations that I can't just feed it directly into the `sqlite-utils` CLI tool.
So I'll use some Python.

<a id="code-snippet--wm-define-imports"></a>
```python
import json

from sqlite_utils import Database
```


## Defining my structures {#defining-my-structures}

Defining a schema is completely optional in sqlite-utils, but I'd like to be explicit about what I'm working with.

[h-cards](/post/2020/04/indieweb-h-cards/) provide the foundation for identifying where entries come from.

<a id="code-snippet--wm-schema-entries"></a>
```python
CARD_SCHEMA = {
    "url": str,
    "name": str,
    "photo": str,
    "type": str,
}
```

<a id="code-snippet--wm-create-tables"></a>
```python
def create_tables(db):
    db["cards"].create(CARD_SCHEMA, pk="url")
    db["entries"].create(
        {
            "url": str,
            "author_card_url": str,
            "published": str,
            "context": str,
            "target": str,
            "type": str,
            "name": str,
            "private": bool,
        },
        pk="url",
        foreign_keys=[
            ("author_card_url", "cards", "url"),
        ],
    )
    db["entry_contents"].create(
        {
            "entry_url": str,
            "text": str,
            "html": str,
        },
        pk=("entry_url", "text", "html"),
        foreign_keys=[
            ("entry_url", "entries", "url"),
        ],
    )
    db["entry_photos"].create(
        {
            "url": str,
            "entry_url": str,
        },
        pk="url",
        foreign_keys=[
            ("entry_url", "entries", "url"),
        ],
    )
    db["entry_rels"].create(
        {
            "canonical": str,
            "entry_url": str,
        },
        pk="canonical",
        foreign_keys=[
            ("entry_url", "entries", "url"),
        ],
    )
    db["entry_summaries"].create(
        {
            "entry_url": str,
            "content-type": str,
            "value": str,
        },
        pk=("entry_url", "content-type", "value"),
        foreign_keys=[
            ("entry_url", "entries", "url"),
        ],
    )
    db["entry_syndications"].create(
        {
            "url": str,
            "entry_url": str,
        },
        pk="url",
        foreign_keys=[
            ("entry_url", "entries", "url"),
        ],
    )
```


## Populating the reactions table {#populating-the-reactions-table}

<a id="code-snippet--wm-save-entry"></a>
```python
def save_entry(webmention, db):
    card = webmention["author"]
    db["cards"].insert(card, pk="url", replace=True)

    entry = {
        "url": webmention["url"],
        "published": webmention["published"],
        "name": webmention.get("name", None),
        "context": webmention["wm-property"],
        "target": webmention["wm-target"],
        "private": webmention["wm-private"],
        "author_card_url": card["url"],
    }
    entry["author_card_url"] = card["url"]
    db["entries"].insert(entry, pk="url", replace=True)

    entry_url = entry["url"]
    entry_content = webmention.get("content", None)
    entry_photos = webmention.get("photo", [])
    entry_rels = webmention.get("rels", None)
    entry_summary = webmention.get("summary", None)
    entry_syndications = webmention.get("syndication", [])

    if entry_content:
        entry_content["entry_url"] = entry_url
        entry_contents = db.table("entry_contents")
        entry_contents.insert(entry_content)

    for photo_url in entry_photos:
        entry_photo = {
            "url": photo_url,
            "entry_url": entry_url,
        }
        db["entry_photos"].insert(entry_photo)

    if entry_rels:
        entry_rels["entry_url"] = entry_url
        db["entry_rels"].insert(entry_rels)

    if entry_summary:
        entry_summary["entry_url"] = entry_url
        db["entry_summaries"].insert(entry_summary)

    for syndication_url in entry_syndications:
        entry_syndication = {
            "url": syndication_url,
            "entry_url": entry_url,
        }
        db["entry_syndications"].insert(entry_syndication)
```

Of course, I need to _load_ the mentions before I can _save_ them.

<a id="code-snippet--wm-load-mentions"></a>
```python
def load_mentions():
    mentions_file = "mentions.jf2"

    with open(mentions_file, "r") as f:
        feed = json.loads(f.read())
        return feed["children"]
```

<a id="code-snippet--wm-define-main"></a>
```python
def main():
    db = Database("mentions.db", recreate=True)
    create_tables(db)
    mentions = load_mentions()

    for entry in mentions:
        save_entry(entry, db)
```

And maybe a nice summary to show what we ended up with?

```shell
sqlite-utils tables mentions.db --counts --table --fmt orgtbl
```

| table    | count |
|----------|-------|
| mentions | 83    |

That's nice, but what kinds of mentions have I been getting, and how many?

```shell
sqlite-utils mentions.db \
    "select distinct(context), count(context) as counted from entries group by context order by counted desc" \
    --table \
    --fmt orgtbl
```


## Static site weirdness {#static-site-weirdness}


### Packing it up for `git` {#packing-it-up-for-git}


### Reinflating? Rehydrating? _Rebuilding_ my database when needed {#reinflating-rehydrating-rebuilding-my-database-when-needed}