---
aliases:
- /coolnamehere/2002/06/02_pagetemplate-history.html
- /post/2002/pagetemplate-history/
date: 2002-06-02T00:00:00Z
tags:
- pagetemplate
title: PageTemplate History
type: post
updated: 2009-07-11T00:00:00Z
year: '2002'
archived_category: coolnamehere
---

I'll admit it. This list is very bad. Nevertheless, I keep telling myself it's better than nothing.
<!--more-->

* Version 1.0
    * Basic logic structure (var, if, and in)
    * Support for multiple Namespaces
* Version 1.1
    * include content from external files
* Version 1.2
    * New Command: unless
    * Added support for CommentCommands
    * Loop Metavariables: `__FIRST__`, `__LAST__`, `__ODD__`
    * include_path can be a list of paths
    * Loosened rules for VariableCommands (check respond_to? rather than has_method?)
    * Lessened penalty for missing files in IncludeCommands (returns an error string rather than raising an exception)
    * Strengthened the system for running in tainted environments.
* Version 2.0
    * Added Preprocessors
        * `[%var sampleCode :escapeHTML %]`
    * Added a CaseCommand
    * Better access of object fields and subfields
* Version 2.1
    * LoopCommands can accept multiple iterators now
    * Added else if functionality
    * New Glossary allows HTML::Template-style syntax.
* Version 2.1.1
    * In-memory caching
* Version 2.1.5
    * Improvements on working with mod_ruby
* Version 2.1.7
    * Added Namespace#delete method
* Version 2.2.0
    * DefineCommand
    * FilterCommand
    * Fixed bug in FileSource#get_filename


