#!/usr/bin/env python3
import context-wordgen as words
import sys

# return error if len(sys.argv) < 4
 
lang = str(sys.argv[1])
oper = str(sys.argv[2])

if oper == "define":
  with open(sys.argv[3]) as wordfile: #I assume it will fail with an error if it's not a valid/existing file
    wordlist = []
    for line in wordfile:
      item = line.split("|")
      #if len(item) > 2:
        # return an error
      wordlist.append(item)
    words.generate(lang, wordlist)


# oper == "translate"
# accesses the stored dictionary to translate words and syntax and apply necessary inflection and sound-change rules
# requires sys.argv[3:] as a string to be translated
# uses trans namespace

# oper == "help"
# what it says on the tin

# other oper ideas:
# "synonym", give a new definition and old definition, use the existing conlang word as old def for new

