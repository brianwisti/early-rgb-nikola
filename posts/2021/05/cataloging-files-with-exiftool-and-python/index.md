---
title: Cataloging files with exiftool and python
slug: cataloging-files-with-exiftool-and-python
description: My ongoing struggle against entropy
caption:
draft: true
tags:
- python
- perl
- tools
date: 2021-05-17
---
## Exiftool

We talked about that the other day.

It's Perl, but we can get at it from Python using PyEXifTool.

## SQLite

Don't think of it as a database.
Think of it as a really good cache.
Okay, it's a little bit of a database.

It supports JSON queries!

## Looking for common fields

- I can maybe use `rowid`.

{{< console >}}
$ exiftool '~/Dropbox/Getting Started.pdf'

ExifTool Version Number         : 11.85
File Name                       : Getting Started.pdf
Directory                       : /home/random/Dropbox
File Size                       : 243 kB
File Modification Date/Time     : 2015:02:17 09:36:41-08:00
File Access Date/Time           : 2020:05:30 14:16:13-07:00
File Inode Change Date/Time     : 2020:05:30 14:16:14-07:00
File Permissions                : rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
⋮
{{< /console >}}

Everything past `MIME Type` looks specific to the file I'm looking at.
So here's my idea.

## The Plan

### Create a SQLite Database

``` sql
CREATE TABLE file (
    FilePath TEXT unique,
    FileBytes INT,
    Directory,
    FileName,
    FileSize,
    MIMEType,
    FileType,
    FileTypeExtension,
    FileCreateDate,
    FileModifyDate,
    FileAccessDate,
    FilePermissions,
    Meta,
    ScanTime INT
);
```

### Populate it with Perl

Because ExifTool

### Explore it with SQLiteBrowser

[How to Find Duplicate Values in a SQL Table]: https://chartio.com/learn/databases/how-to-find-duplicate-values-in-a-sql-table/

``` sql
CREATE VIEW duplicate AS
SELECT a.*
FROM file a
join (
  SELECT FileBytes, MIMEType, count(*) AS FileCount
  FROM FILE
  GROUP BY FileBytes, MIMEType
  HAVING FileCount > 1
)
ON a.FileBytes = b.FileBytes
  AND a.MIMEType = b.MIMEType
order by a.FileBytes, a.FilePath;
```

### Explore it with Python

Because Datasette