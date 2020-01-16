---
aliases:
- /blogspot/2011/04/14_elaborate-answers-to-simple-questions.html
- /post/2011/elaborate-answers-to-simple-questions/
categories:
- Blogspot
date: 2011-04-14T00:00:00Z
tags:
- python
title: Elaborate Answers To Simple Questions
type: post
year: '2011'
---
<p><strong>tl;dr</strong>: Use <tt>string</tt> methods instead of importing <tt>string</tt>. Build email messages with the standard <a href="http://docs.python.org/library/email.html">email</a> library.</p>
<!--more-->

<p>I saw an email last night from somebody with a simple <a href="http://python.org">Python</a> question.</p>

<blockquote markdown="1">
<p>Hi,</p>
 
<p>... I have some issues in my python program. I have installed python27 in C:\Python27.
I started learning python with small programs. I’m saving all python programs in C:\ROUGH
When I am executing these scripts through command prompt facing some problem with "import". Please help me out</p>

<p>My program:</p>

<pre>
#!python
import sys
#import C:\Python27\Lib\string
import string
   
Subject = "Testmail"
To = "yeahright@nonotreallyawebsiteihope.com"
From = "yeahright@nonotreallyawebsiteihope.com"
text = "Test"
body = string.join(("From: %s" % From,
                    "To: %s" % To,
                    "Subject: %s" %Subject,
                    text
                    ),"\r\n")
     
print body
</pre>

<p>ERROR IS:</p>

<pre>
C:\Python27>python.exe c:\ROUGH\addingsubtofrm.py
Traceback (most recent call last):
  File "c:\ROUGH\addingsubtofrm.py", line 12, in <module>
    body = string.join(("From: %s" % From,
AttributeError: 'module' object has no attribute 'join'
</pre>

<p>...</p>
</blockquote>

<p>For some reason, I do not get any error when I try to run her code with Python 2.7.1 on Windows XP. That's okay, though. I can still help a little bit on the style.</p>

<p>Although <tt>join</tt> is part of the <tt><a href="http://docs.python.org/library/string.html">string</a></tt> module, it is also directly attached to strings. So instead of using <tt>string.join(items, separator)</tt>, you could use <tt>separator.join(items)</tt>. That's considered the standard way to join a list of items into a single string these days.</p>

``` python
Subject = "Testmail"
To = "yeahright@nonotreallyawebsiteihope.com"
From = "yeahright@nonotreallyawebsiteihope.com"
text = "Test"
body = "\r\n".join(("From: %s" % From,
                    "To: %s" % To,
                    "Subject: %s" %Subject,
                    text
                    ))
print body
```

<p>This probably answers her question, but I am apparently in the mood to spend a lot of time writing about Python basics. Sounds like blog gold to me.</p>

<p>There's a problem with <tt>body</tt> if you want to use it for an actual email message. There needs to be a blank line between the headers and the body. One way to do that is to use <tt>join</tt> twice: once to build the header block and again to create a properly laid-out email message.</p>

``` python
Subject = "Testmail"
To = "yeahright@nonotreallyawebsiteihope.com"
From = "yeahright@nonotreallyawebsiteihope.com"

text = "Test"

header_block = "\r\n".join((
    "From: %s" % From,
    "To: %s" % To,
    "Subject: %s" % Subject
    ))

# A full email has a blank line between the header block and the message body
body = "\r\n\r\n".join((header_block, text))
print body
```

<p>The header block still looks a little clumsy. I am sure there is a prettier way to generate it. When I look at how the header block is printed, I realize that it looks a lot like a Python dictionary. Does the code look any clearer if I use a dictionary?</p>

``` python
headers = {
    "Subject": "Testmail",
    "To": "yeahright@nonotreallyawebsiteihope.com",
    "From": "yeahright@nonotreallyawebsiteihope.com"
}

text = "Test"

# Each line of a header block contains a single email header,
# which looks like "Header-Field: Header-Value"
header_block = "\r\n".join(("From: %s" % headers['From'],
                            "To: %s" % headers['To'],
                            "Subject: %s" % headers['Subject']))

# A full email has a blank line between the header block and the message body
body = "\r\n\r\n".join((header_block, text))

print body
```

<p>Well, no. Not really. I think I'm actually typing <em>more</em> than I was before, and it's not really any easier to read. It's all that <tt>"From: %s" % headers['From']"</tt> nonsense.</p>

<p>`join` takes a sequence. I do not have to hand it a literal like we have been doing so far. Let's build a list of header lines, and *then* join them.</p>

``` python
headers = {
    "Subject": "Testmail",
    "To": "yeahright@nonotreallyawebsiteihope.com",
    "From": "yeahright@nonotreallyawebsiteihope.com"
}

text = "Test"

# Each line of a header block contains a single email header,
# which looks like "Header-Field: Header-Value"
header_lines = []

for field, value in headers.items():
    header_line = "%s: %s" % (field, value)
    header_lines.append(header_line)
      
header_block = "\r\n".join(header_lines)

# A full email has a blank line between the header block and the message body
body = "\r\n\r\n".join((header_block, text))

print body
```

<p>It is easier to read, even if it is a little longer. We are building a list of header lines by stepping through each of the key/value pairs that make up the <tt>headers</tt> dictionary. Oh, and don't worry about what order the items are printed in. That order doesn't matter in email messages.</p>

<p>One thing - and this is a little thing - is that it takes us four lines of code to build the list. Like I said, it's a little thing. But building lists like this is so common that Python provides powerful tools called <a href="http://docs.python.org/tutorial/datastructures.html#list-comprehensions">list comprehensions</a>, which can reduce those four lines into one.</p>

``` python
headers = {
    "Subject": "Testmail",
    "To": "yeahright@nonotreallyawebsiteihope.com",
    "From": "yeahright@nonotreallyawebsiteihope.com"
}

text = "Test"

# Each line of a header block contains a single email header,
# which looks like "Header-Field: Header-Value"
header_lines = ["%s: %s" % (field, value) for (field, value) in headers.items()]  
header_block = "\r\n".join(header_lines)

# A full email has a blank line between the header block and the message body
body = "\r\n\r\n".join((header_block, text))

print body
```

<p>All right. Now if this were an <em>actual</em> email, there are some missing headers. There are probably also some details missing that are related to email handling. Rather than try to figure out what's missing, I'm going to suggest that you use the <a href="http://docs.python.org/library/email.html"><tt>email</tt></a> library that comes standard with Python.</p>

``` python
from email.mime.text import MIMEText

headers = {
    "Subject": "Testmail",
    "To": "yeahright@nonotreallyawebsiteihope.com",
    "From": "yeahright@nonotreallyawebsiteihope.com"
}

text = "Test"

msg = MIMEText(text)
for field, value in headers.items():
    msg[field] = value

print msg.as_string()
```

<p>And what does the end result look like?</p>

``` http
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
To: yeahright@nonotreallyawebsiteihope.com
From: yeahright@nonotreallyawebsiteihope.com
Subject: Testmail

Test
```

<p>There you go. If your end goal is generating emails, use the Python email library.</p>
