# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Lists are mutable and tuples are immutable meaning tuples can not be changed.  If entries have different meanings, then tuples should be used.  Tuples work as keys in dictionaries since they are immutable.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Lists keep the element's order and sets do not.  Sets require items to be hashable while lists do not.  Sets can't have duplicates, lists can.  

>An example of using a list is for an ordered collection of items like a list of phone numbers of new tenants in a building.
>An example of using a set is for an unordered set of items like the set of all words in a document.

>Sets are faster when determining if an object is present.   This is because sets are implemented using hashtables.  When objects are added to a set, its position is determined by the hash of added object.  To see if the object exits in the set, the program looks if its at the position determined by its hash.  

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>Lambda functions are functions that are defined with one line.  It is used to defined a function without having to name the function. It is best used for simple functions that are not to be reused to avoid lots of one line functions in the code.

>An example of using lambda functions in key argument to sorted function:
sorted(sorttuples, key = lamba x:x[1]).  This sorts the tuples by each tuple's 2nd element.

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>List comprehensions are a simplifed way of creating a list instead of using a for loop to do so.

>An example is: 
wil=[1,2,3,4]
x = [i**2 for i in wil]

>Its equivalent using 'map' is:
wil=[1,2,3,4]
list(map((lambda x: x**2), wil))




---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
