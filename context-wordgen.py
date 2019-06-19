#!/usr/bin/env python3
from genling import *
from random import randint

def phonemize(item):
  pw = item.split(",")
  return Phoneme(pw[0],pw[1])

def generate(lang, wordlist):
  syllables = []
  phonemes = []
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
    syl_struct = f[0]
    syl_bounds = f[1]
    syl_balance = f[2].split(",")
    
  filters = []
  with open(lang+"/filters/simple.txt","r") as f:
    for line in f:
      filters.append(SimpleFilter(line))
  with open(lang+"/filters/regex.txt","r") as f:
    for line in f:
      filters.append(RegexFilter(line))

  for i,x in enumerate(syl_struct):
    if x is "C":
      syllables.append(Syllable(consonants))
    elif x is "V":
      syllables.append(Syllable(vowels))
    else:
      dice = randint(0,9)
      if dice < x:
        syllables.append(Syllable(consonants))
      else:
        syllables.append(Syllable(vowels))
        
  stem = Stem(syllables, balance=syl_balance, filters=filters,
    prefix=syl_bounds[0], infix=syl_bounds[1], suffix=syl_bounds[2])

  for worddef in wordlist:
    pos, word = worddef.split("|")
    newword = stem.generate()
    # use pos to apply appropriate Word rules
    # store new word info in dictionary db