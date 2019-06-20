#!/usr/bin/env python3
import context_wordgen as words
import sys
import sqlite3
from pathlib import Path

# return error if len(sys.argv) < 3
lang = str(sys.argv[1])
oper = str(sys.argv[2])

if oper == "create":
  # error if sys.argv[3] isn't set
  print("creating new words")
  wordlist = []
  with open(sys.argv[3]) as wordfile: #I assume it will fail with an error if it's not a valid/existing file
    for line in wordfile:
      wordlist.append(line)
  
  newlist = words.generate(lang, wordlist)
  # each item in newlist: item[0] def, item[1] pos, item[2] created word in raw format
  # save to database

# oper == "define"
# allows you to add new entries directly to the dictionary without having to mess with db software
# requires sys.argv[3] as a filename of definitions

# oper == "translate"
# accesses the stored dictionary to translate words and syntax and apply necessary inflection and sound-change rules
# requires sys.argv[3:] as a string to be translated
# uses trans namespace

# oper == "initialize"
# creates a skeleton directory for a new language; dir must not already exist
# also initializes database

if oper == "initialize":
  dir = Path(lang)
  try:
    dir.mkdir()
  except FileExistsError:
    sys.exit(lang+" directory already exists")

  Path(lang+"/phonemes.txt").touch()
  Path(lang+"/syllables.txt").touch()
  Path(lang+"/sound_changes.txt").touch()
  Path(lang+"/filters").mkdir()
  Path(lang+"/filters/simple.txt").touch()
  Path(lang+"/filters/regex.txt").touch()
  
  try:
    conn = sqlite3.connect(lang+"/dictionary.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE WORDS
             ([id] INTEGER PRIMARY KEY,[definition] text, [part_of_speech] text, [spoken] text, [written] text)''')
    conn.commit()
  except sqlite3.Error as e:
    print(e)
  finally:
    conn.close()
  print("Directory for new language "+lang+" successfully initialized")

# oper == "help"
# what it says on the tin

# other oper ideas:
# "synonym", give a new definition and old definition, use the existing conlang word as old def for new

