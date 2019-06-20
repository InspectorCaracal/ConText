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
  conn = sqlite3.connect(lang+"/dictionary.db")
  c = conn.cursor()
  for item in wordary:
    print(item)
    print(get_word(c,item)+"\n")
  conn.close()