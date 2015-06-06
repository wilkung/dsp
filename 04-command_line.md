# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> Created MS-Word document with cheat sheet of all commands as well as a shorter version for less often used commands i might need to reference more often

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>ls -- list contents of the current working directory (folders & files)  
>ls -a -- list all contents of current working directory (including hidden files)  
>ls -l -- list contents of current working directory with details (size, modified date, owner of files & permissions)  
>ls -lh -- list contents of current working directory with details in "human readable" format (file sizes not in byte sizes, but using KB, MB, GB notations)  

---


---

What does `xargs` do? Give an example of how to use it.

>xargs is to execute arguments for an input command.  

>Say in the case of using echo to print numbers, you want to print every 5 numbers in a sequence on a separate line.  

>Without using xargs, you might send:  
>echo {1..5}  
>echo {6..10}  
>echo {11..15}  
>echo {16..20}  

>Using xargs, you could issue one line to handle this:  
>echo {1..20} | xargs -n 5

---
