#!/usr/bin/env python3
from genling import *
import sqlite3

def get_word(c,definition,pos=False):
  if pos is False:
    query = "SELECT raw FROM words WHERE definition=?"
    c.execute(query, (definition,) )
  else:
    query = "SELECT raw FROM words WHERE definition=? AND part_of_speech=?"
    c.execute(query, (definition, pos) )
  result = c.fetchall()
  return result
  
  
def process(lang,wordary):
  try:
    conn = sqlite3.connect(lang+"/dictionary.db")
  except sqlite3.Error as e:
    return e
    
  written = []
  pronunc = []
  
  # syllable bounds for cleanup
  with open(lang+"/syllables.txt","r") as f:
    lines = f.readlines()
    syl_bounds = lines[1]
  cleanup = []
  for x in syl_bounds:
    cleanup.append(SimpleReplace(x,""))
  
  # grammar parsing
  grammar = {}
  with open(lang+"/grammar/simple.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      item = line.split("|",1)
      if len(item) > 1:
        rep = item[1].split(",",1)
        if len(rep) > 1:
            grammar[item[0]] = SimpleReplace(rep[0],rep[1].strip())
  with open(lang+"/grammar/regex.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      item = line.split("|",1)
      if len(item) > 1:
        rep = item[1].split(",",1)
        if len(rep) > 1:
            grammar[item[0]] = RegexReplace(rep[0],rep[1].strip())
  
  # writing system replacements from raw
  writing = []
  with open(lang+"/writing/simple.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",",1)
      if len(rep) > 1:
        writing.append(SimpleReplace(rep[0],rep[1].strip()))
  with open(lang+"/writing/regex.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",",1)
      if len(rep) > 1:
        writing.append(RegexReplace(rep[0],rep[1].strip()))
  writ_word = Word(writing + cleanup)

  # pronunciation change replacements from raw
  reading = []
  with open(lang+"/sound_changes/simple.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",",1)
      if len(rep) > 1:
        reading.append(SimpleReplace(rep[0],rep[1].strip()))
  with open(lang+"/sound_changes/regex.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",",1)
      if len(rep) > 1:
        reading.append(RegexReplace(rep[0],rep[1].strip()))
  read_word = Word(cleanup + reading)

  c = conn.cursor()
  for item in wordary:
  # process for grammar
    parts = item.split("+")
    nuwords = get_word(c,parts[0])
    pwords = []
    wwords = []
    for word in nuwords:
      if len(parts) > 1:
        nuword = grammar[parts[1]].apply(word[0])
      else:
        nuword = word[0]
      pwords.append(read_word.create(nuword))
      wwords.append(writ_word.create(nuword))
    pwords = "|".join(pwords)
    wwords = "|".join(wwords)
    if len(nuwords) > 1:
      pwords = "("+pwords+")"
      wwords = "("+wwords+")"
    pronunc.append(read_word.create(pwords))
    written.append(writ_word.create(wwords))
  conn.close()
  print(' '.join(wordary))
  print("spoken: "+' '.join(pronunc))
  print("written: "+' '.join(written))
