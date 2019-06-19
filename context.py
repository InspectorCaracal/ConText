#!/usr/bin/env python3
import context-wordgen as words
import sys

# return error if len(sys.argv) < 4
 
lang = str(sys.argv[1])
oper = str(sys.argv[2])

# oper == "define"
# generates new words and assigns them to meanings in a list
# requires sys.argv[3] of a file containing a list of part of speech|definition pairs separated by lines
# uses words namespace

# oper == "translate"
# accesses the stored dictionary to translate words and syntax and apply necessary inflection and sound-change rules
# requires sys.argv[3:] as a string to be translated
# uses trans namespace

# oper == "help"
# what it says on the tin

# other oper ideas:
# "synonym", give a new definition and old definition, use the existing conlang word as old def for new

