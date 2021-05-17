---
title: VS Code pylint needs pylintrc
slug: vs-code-pylint-needs-pylintrc
date: 2020-03-19 10:15:30-07:00
tags:
- python
- vscode
- editors
uuid: 00d872c4-77d7-462a-a830-e864e174a066
aliases:
- /note/2020/79/vs-code-pylint-needs-pylintrc/
category: note
type: micro
---
[Visual Studio Code](https://code.visualstudio.com/) doesn’t seem to
pick up my environment’s
[PYTHONPATH](https://docs.python.org/3.8/using/cmdline.html#envvar-PYTHONPATH)
when running [pylint](https://www.pylint.org/). Makes project-local
modules a headache. The solution: put it in your pylint config.

{{< code file="${workspaceFolder}/.pylintrc" lang="ini" >}}
[MASTER]
init-hook='import sys; sys.path.append("pylib")'
{{< /code >}}

Okay, I got more planned for today than messing with code. Back to that
other stuff.