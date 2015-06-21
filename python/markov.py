#!/usr/bin/env python

# use one words
# starts with first word
# lowercase all words
# keep punctuations

import sys
import random
#count = 200

docname = sys.argv[1]
count = sys.argv[2]

text_file = open(docname, "r")
lines = text_file.read().split()
lines = [x.lower() for x in lines]
print lines
print len(lines)
text_file.close()

DOIdict = {}
for i in range(0,len(lines)-1):
    if lines[i] in DOIdict:
        DOIdict.setdefault((lines[i]),[]).append(lines[i+1])
    else:
        DOIdict.setdefault((lines[i]),[]).append(lines[i+1])

firstword = 'when'
pseudoDOI = []
pseudoDOI.append(firstword)

for x in range(0,100):
    pseudoDOI.append( random.choice(DOIdict[pseudoDOI[x]]) )
    
print pseudoDOI
