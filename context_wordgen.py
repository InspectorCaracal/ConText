#!/usr/bin/env python3
from genling import *
from random import randint

def phonemize(item):
  pw = item.split(",")
  return Phoneme(pw[0],int(pw[1]))

def generate(lang, wordlist):
  syllables = []
  phonemes = []
  segments = []
  syl_struct = ''

  with open(lang+"/phonemes.txt","r") as f:
    for line in f:
      phonelist = line.split("|")
      phonelist = list(map(phonemize,phonelist))
      phonemes.append(phonelist)

  vowels = phonemes[0]
  consonants = phonemes[1]
  
  syl_balance = []

  with open(lang+"/syllables.txt","r") as f:
    lines = f.readlines()
    syl_struct = lines[0]
    syl_bounds = lines[1]
    syl_balance = list(map(int,lines[2].split(",")))
    
  filters = []
  with open(lang+"/filters/simple.txt","r") as f:
    for line in f:
      filters.append(SimpleFilter(line))
  with open(lang+"/filters/regex.txt","r") as f:
    for line in f:
      filters.append(RegexFilter(line))

  for x in syl_struct:
    if x is "C":
      segments.append(Segment(consonants))
    elif x is "V":
      segments.append(Segment(vowels))
    elif x.isdigit():
      dice = randint(0,9)
      if dice < int(x):
        segments.append(Segment(consonants))

  syllables = [ Syllable(segments) ]
        
  stem = Stem(syllables, balance=syl_balance, filters=filters,
    prefix=syl_bounds[0], infix=syl_bounds[1], suffix=syl_bounds[2])
    
  cleanup = []
  for x in syl_bounds:
    cleanup.append(SimpleReplace(x,""))

  for worddef in wordlist:
    pos, word = worddef.split("|")
    #if len(item) > 2:
      #return an error
    newword = stem.generate()
    print(word, newword)
    # use pos to apply appropriate Word rules
    # store new word info in dictionary db