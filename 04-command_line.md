# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> This is a work in progress:

>ls 	  list directory

>cd	    change directory

>pwd	  show current directy

>mkdir  create new directory

>rm	    delete file

>cp	    copy file

>mv	    rename file

>cat	  puts standard input into file

>more	  shows content of file

>head	  shows top 10 lines of file

>tail	  shows last 10 lines of file

>grep	  search for a pattern in a file

>tar	  creates tar

>gzip	  compresses file and renames it

>Ctrl+C	stops current command

>exit	  logs out of session



---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>ls lists items in your current directory. 

>ls -a option flag lists all files including hidden files starting with '.'

>ls -l lists files using a long list format.

>ls -lh lists files with their size

>combining -a and -lh is meaningful in that it will give sizes of the hidden files as well


---


---

What does `xargs` do? Give an example of how to use it.

>The xargs command is used in with the find and grep commands to divide a large list of arguments into a smaller list received from standard input.

>Here is an example of its use that I found on stackexchange:
>find /foot/bar/ -name '*.mp4' -print0 | xargs -0 mv -t /some/path
---
