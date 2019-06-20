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
  result = c.fetchone()
  return result[0]
  
  
def process(lang,wordary):
  try:
    conn = sqlite3.connect(lang+"/dictionary.db")
  except sqlite3.Error as e:
    return e
    
  written = []
  pronunc = []
  
  with open(lang+"/syllables.txt","r") as f:
    lines = f.readlines()
    syl_bounds = lines[1]

  cleanup = []
  for x in syl_bounds:
    cleanup.append(SimpleReplace(x,""))
  pro_word = Word(cleanup)
  
  writing = []
  with open(lang+"/writing/simple.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",")
      if len(rep) > 1:
        writing.append(SimpleReplace(rep[0],rep[1].strip()))
  with open(lang+"/writing/regex.txt","r", encoding='utf-8-sig') as f:
    for line in f:
      rep = line.split(",")
      if len(rep) > 1:
        writing.append(RegexReplace(rep[0],rep[1].strip()))
  writ_word = Word(cleanup + writing)

  c = conn.cursor()
  for item in wordary:
  # process for grammar
    nuword = get_word(c,item)
    pronunc.append(pro_word.create(nuword))
    written.append(writ_word.create(nuword))
  conn.close()
  print(' '.join(wordary))
  print("spoken: "+' '.join(pronunc))
  print("written: "+' '.join(written))
