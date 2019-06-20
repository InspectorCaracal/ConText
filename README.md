# ConText
a tool for creating and working with constructed languages

credit to [genling](https://github.com/2sh/genling) as the word-generator library I'm using

*this documentation is still in progress*

### To-Do

- Properly handle synonyms in translated sentences.
- Alternate translation syntax of `translate --files input.txt output.txt`
- Add manual vocab addition instead of purely generated vocabulary
- `help` command
- fill all the files in the example language with at least two items
- different syllable balances for different parts of speech (most significantly so articles and pronouns can be biased towards fewer syllables)

## Installation
1. Make sure you have Python 3 installed, preferably the version that comes with pip
2. `pip install genling`
3. Clone or download this repository to wherever you want the tool installed.

## Usage
Basic syntax: `python context.py [language] [command] [parameters]`

### initialize
`python context.py [language] initialize`

Builds a new skeleton directory named `[language]`, where you can then enter all of your language's phonemes and other rules. See the **Language Files** section for details on the contents of this directory. 

### create
`python context.py [language] create [filename]`

Takes a file containing a list of definitions, generates new words for the definitions and adds them to the database. Definitions cannot include spaces. See `create_example.txt` for an example of how the file is structured.

### translate
`python context.py [language] translate [sentence or phrase]`

Takes a string of words to be translated. Grammatical changes are attached by a + and part of speech with a . (not yet implemented). You have to get your word order right on your own, sorry!

ex.
`the cat.n+NOM.SG walk.v+PAST`

This will eventually have an alternative usage where you can provide it with two file names and it will take the first and write the results to the second.

### not yet implemented
`python context.py [language] define [filename]`
Like create, except you provide your own raw conlang words to add to the database.

`python context.py help`
What you'd expect in a help command.


## Language Files
Create a directory for your language: this will be the term you use to reference your language when you work with it. e.g. if you have a language named *bob* then you want to make a directory `bob/` and run the script as `context.py bob [other stuff]`

### Phonemes
The phonemes file goes in your language directory, named `phonemes.txt`

Phoneme sets are divided by lines. If you have an optional consonant place, define a placeholder "blank" character in the list of consonants.

The first line is your vowels. Your second line is your consonants.

Each phoneme set is divided into a "grapheme" and "weight" pair. The grapheme is just how you personally want to represent your phonemes: it could be an IPA character, for example, or it could just be regular letters like "th". The weight is a number indicating how likely that phoneme is to show up. Higher numbers mean more likely.

An example vowel phoneme set might look like:

`a,2|e,5|i,3|y,5|o,4|ou,1|u,1`

### Syllable Structure
The rules for your syllable structures go in a file in your language directory, named `syllables.txt`.

The first line are your vowel/consonant patterns. Divide all possible syllable patterns by | separators. If you want to have different frequencies for the different patterns, you can add a weight after them with a comma.

ex. 1
`CV|CVC|CCVC`

ex. 2
`CV,8|CVC,4|CCVC,1`

### Filters
Rules about what phoneme patterns and combinations can't happen. These are in your language directory in a subdirectory, `filters`

`filters/simple.txt` is a list of simple combinations that can't exist. For example, if you can't end a word in an x and your word end-boundary character is >, you can enter `x>` as a line in simple.txt - or if you can't have a b and a q next to each other, and your syllable boundary is |, then you can enter two lines: `b|q` and `q|b` to prevent that combination.

`filters/regex.txt` is where you can define more complex rules as regular expressions.

### Sound changes
Rules for changes in *pronunciation only*. They will not affect how the word is written or the raw word data, which allows the sound changes to vary between the raw stem form and the grammatically inflected form. These are located in a subdirectory in your language directory, `sound_changes`

`sound_changes/simple.txt` is a list of simple replacements, each on their own line. For example, if you want to drop ʃ when it occurs after ʧ, you could add a line: `ʧʃ,ʧ`

`sound_changes/regex.txt` is where you can define more complex mutations and replacements as regular expressions. This is also how you can change the sound of phonemes at the beginning or end of a word.

### Writing
The writing system for your language to be written in goes in a subdirectory of your language directory, named `writing`

`writing/simple.txt` is a list of simple phoneme replacements, each on their own line. For example, if you have θ in your phonemes but want it to be written as th: `θ,th`

`writing/regex.txt` is where you can define more complex replacements as regular expressions.