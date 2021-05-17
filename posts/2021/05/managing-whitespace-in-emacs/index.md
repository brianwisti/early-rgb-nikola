---
title: Managing Whitespace in Emacs
description: In which I see tabs and spaces so I can pick one
draft: true
tags:
- emacs
- packages
- tools
uuid: cd188109-f955-404e-86df-3ab2ab87c9c3
date: 2021-05-17
previewimage: /images/2021/05/managing-whitespace-in-emacs/cover.png
---
{{< aside title="tl;dr" >}}
I don’t know yet.
{{< /aside >}}

## Goals

Show me the whitespace. But not too garish. I don’t want it distracting
from when I’m writing, but I do want to see what I’m working with.

- understand the visual language used
- Automatically load whitespace-mode for text and code

## whitespace-mode

- a core emacs mode
- shows whitespace
- shows trouble spots
    - blank lines at the beginning and end of your file
    - indentation — when you’re mixing tabs and spaces *too* much
    - trailing whitespace
    - empty lines with whitespace
- can configure to only look for the whitespace issues you care about
- can fix the whitespace issues it finds

Figured out the details by looking up random [blog
posts](https://writepermission.com/emacs-package-use-package-hydra.html)
and seeing what I can use.

## The useful bits

``` elisp
(use-package whitespace
  :ensure t
  :preface
  (defun bmw/whitespace-mode ()
    (unless (eq major-mode 'org-mode)
      (progn
        (whitespace-mode)
        (bmw/theme-whitespace))))
  :custom
  (whitespace-action '(auto-cleanup))
  (whitespace-line-column 120)
  (whitespace-style
   '(face lines trailing empty tabs spaces indentation space-mark tab-mark))
  :hook
  ((prog-mode text-mode) . bmw/whitespace-mode))
```

### What this looks like

![whitespace showing whitespace](cover.png)

## Cleaning whitespace

  - thanks to the hook, happens automatically on write

![cleaned up](whitespace-fixed.png)

### Manually

    M-x whitespace-clean

## The cosmetic bits

### Disable for org mode

Honestly I should just disable whitespace for org mode. It gets in the
way and messes up themes with variable fonts.

### A little less garish please

{{< note >}}
I want to learn enough ELisp to get `face-attribute` working with
use-package's `:custom-face`. Until then, `set-face-attribute` in the
`:config` section did what I needed.
{{< /note >}}

``` elisp
(defun bmw/color-dim (steps)
  (apply 'color-rgb-to-hex
         (car (color-gradient
               (color-name-to-rgb (face-attribute 'default :background))
               (color-name-to-rgb (face-attribute 'default :foreground))
               steps))))

(defun bmw/theme-whitespace ()
  "Apply my own face-attribute changes after loading a custom theme"
  (set-face-attribute 'whitespace-indentation nil
                      :background (face-attribute 'error :background)
                      :foreground (face-attribute 'error :foreground))
  (set-face-attribute 'whitespace-tab nil
                      :background (face-attribute 'font-lock-comment-face :background)
                      :foreground (face-attribute 'font-lock-comment-face :foreground))
  (set-face-attribute 'whitespace-space nil
                      :background (face-attribute 'font-lock-comment-face :background)
                      :foreground (bmw/color-dim 3)))

(use-package whitespace
  :ensure t
  :preface
  (defun bmw/whitespace-mode ()
    (unless (eq major-mode 'org-mode)
      (progn
        (whitespace-mode)
        (bmw/theme-whitespace))))
  :custom
  (whitespace-action '(auto-cleanup))
  (whitespace-line-column 120)
  (whitespace-style
   '(face lines trailing empty tabs spaces indentation space-mark tab-mark))
  :hook
  ((prog-mode text-mode) . bmw/whitespace-mode))
```

- explain whitespace variables and functions