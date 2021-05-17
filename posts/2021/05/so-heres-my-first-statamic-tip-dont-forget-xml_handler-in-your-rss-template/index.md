---
title: "So here's my first Statamic tip: don't forget xml_handler in your RSS template"
date: 2021-05-08
tags:
- site
- statamic
- I fixed it!
category: note
type: micro
---
{{< twitter "1390887717261561857" >}}

Yeah, the link was there: [/index.xml](/index.xml).
It just wasn't outputting valid XML until I replaced my raw `<?xml` with the `xml_handler` tag:

```
{{ xml_handler }}
```

Should be all better now.
Or at least better than it was.