AutoSyntax
==========

Automatically set syntax in Sublime Text files

Currently just checks the **first line** to match any: 

* `# vi: set ft=language :`
* `# -*- mode: language -*-`

and sets the syntax.

Basically I just got tired of opening files like `Vagrantfile` and seeing the top of the files has: `# vi: set ft=ruby :` but still having to manually set the syntax to ruby.
