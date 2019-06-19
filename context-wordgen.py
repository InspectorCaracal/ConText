#!/usr/bin/env python3
from genling import *

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

  init_segments = []
  segments = []
  final_segments = []
  
  vowels = phonemes[0]
  consonants = phonemes[1]
  word_initial = phonemes[2] if len(phonemes) > 2 else None
  word_final = phonemes[3] if len(phonemes) > 3 else None
  
  # index+1 is syll number, value is weight
  syllable_balance = [5, 2]

  # process filter rules here
  #  syl_struct = f[0]

  for i,x in enumerate(syl_struct):
    if i == 0 and word_initial not None:
      syllables.append(Syllable(word_initial, position=1))
    elif i == len(syl_struct)-1 and word_final not None:
      syllables.append(Syllable(word_final, position=-1))
    else:
      if x is "C":
        syllables.append(Syllable(consonants, position=[1,-1]))
      elif x is "V":
        syllables.append(Syllable(vowels, position=[1,-1]))
        
#  stem = Stem(syllables, balance=syllable_balance, filters=filters, prefix="<", infix="#", suffix=">")

  for worddef in wordlist:
    pos, word = worddef.split("|")
    newword = stem.generate()
    # use pos to apply appropriate Word rules
    # store new word info in dictionary db