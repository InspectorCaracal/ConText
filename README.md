# ConText
a tool for creating and working with constructed languages

Full documentation will be in eventually. Right now this is just notes on usage as I go.

## Language Files
Create a directory for your language: this will be the term you use to reference your language when you work with it. e.g. if you have a language named *bob* then you want to make a directory *bob/* and run the script as *context.py bob [other stuff]*

### Phonemes
The phonemes file goes in your language directory, named *phonemes.txt*

Phoneme sets are divided by lines. If you have an optional consonant place, define a placeholder "blank" character in the list of consonants.

The first line is your vowels. Your second line is your general or mid-word consonants. If you have a different set of consonants for the beginning or end of a word, that goes on the next two lines. *Even if you only have one*. Just copy your regular consonant line to the one that doesn't get a special case.

Recap:
1. Vowels
2. Consonants
3. Word-initial consonants
4. Word-final consonants

Each phoneme set is divided into a "grapheme" and "weight" pair. The grapheme is just how you personally want to represent your phonemes: it could be an IPA character, for example, or it could just be regular letters like "th". The weight is a number indicating how likely that phoneme is to show up. Higher numbers mean more likely.

An example vowel phoneme set might look like:

a,2|e,5|i,3|y,5|o,4|ou,1|u,1

### Syllable Structure
The rules and filters for your syllable structures go in a subdirectory in your language directory, named *rules/*

Filters also go here: *simple_filters.txt* is simple phoneme combinations that can't exist in your language. *regex_filters.txt* is where you can define more complex filters as regular expressions

### Writing
The writing system for your language's phonemes to be written as go in a file in your language directory, named *writing.txt*