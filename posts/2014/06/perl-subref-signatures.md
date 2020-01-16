---
aliases:
- /programming/2014/06/25_perl-subref-signatures.html
- /post/2014/perl-subref-signatures/
categories:
- programming
date: 2014-06-25T00:00:00Z
tags:
- perl
title: Perl 5.20 Signatures in Subroutine References
type: post
year: '2014'
---
[Perl]: http://perl.org
[Perl][] 5.20 has experimental support for function signatures. That's good 
news. I just thought to check if signatures can be used in subroutine 
references. They can.
<!--more-->

~~~ perl
# Set a base set of features.
use 5.20.0;

# Signatures are experimental, so are not enabled by default.
use feature 'signatures';

# Otherwise Perl will warn about using the experimental feature
no warnings 'experimental::signatures';

sub hello($person) {
  say "Hello, $person";
}

my $goodbye = sub($person) {
  say "Goodbye, $person";
};

my $me = "Brian";

hello( $me );
$goodbye->( $me );
~~~ 

It's a simple test. Just checking to see if I can maybe use this feature in 
my own projects.

~~~ console
$ perl sig-test.pl
Hello, Brian
Goodbye, Brian
~~~ 

[Pygments]: http://pygments.org/

This pleases me. It's not going to make life easier for [Pygments][], though.
