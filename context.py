#!/usr/bin/env python3
import context_wordgen as words
import context_translate as trans
import sys
import sqlite3
from pathlib import Path

if len(sys.argv) < 3:
  sys.exit("Insufficient arguments")

lang = str(sys.argv[1])
oper = str(sys.argv[2])

if oper == "create":
  if not Path(lang).is_dir():
    sys.exit("Language directory for "+lang+" does not exist.")
  # error if sys.argv[3] isn't set
  chk = Path(sys.argv[3]).is_file() if len(sys.argv) > 3 else None
  if chk is None or chk is False:
    sys.exit("Invalid filename provided for word list.")
  print("creating new words")
  wordlist = []
  with open(sys.argv[3]) as wordfile: #I assume it will fail with an error if it's not a valid/existing file
    for line in wordfile:
      wordlist.append(line)
  
  if words.generate(lang, wordlist):
    print("\nWords added to dictionary.")

# oper == "define"
# allows you to add new entries directly to the dictionary without having to mess with db software
# requires sys.argv[3] as a filename of definitions

if oper == "translate":
  if not Path(lang).is_dir():
    sys.exit("Language directory for "+lang+" does not exist.")
  phrase = sys.argv[3:] if len(sys.argv) > 3 else None
  if phrase is None:
    sys.exit("Nothing to translate!")
  trans.process(lang,phrase)
  
  
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
  Path(lang+"/filters").mkdir()
  Path(lang+"/filters/simple.txt").touch()
  Path(lang+"/filters/regex.txt").touch()
  Path(lang+"/writing").mkdir()
  Path(lang+"/writing/simple.txt").touch()
  Path(lang+"/writing/regex.txt").touch()
  Path(lang+"/sound_changes").mkdir()
  Path(lang+"/sound_changes/simple.txt").touch()
  Path(lang+"/sound_changes/regex.txt").touch()
  
  try:
    conn = sqlite3.connect(lang+"/dictionary.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE words
      ([id] INTEGER PRIMARY KEY AUTOINCREMENT,
       [definition] TEXT, [part_of_speech] TEXT, [raw] TEXT)""")
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

