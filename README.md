# ConText
a tool for creating and working with constructed languages

credit to [genling](https://github.com/2sh/genling) as the word-generator library I'm using

Full documentation will be in eventually. Right now this is just notes on usage as I go.

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

*Sound changes, as opposed to phonetic taboos, are handled elsewhere and have not been added yet.*

### Writing
The writing system for your language to be written in goes in a subdirectory of your language directory, named `writing`

`writing/simple.txt` is a list of simple phoneme replacements, each on their own line. For example, if you have θ in your phonemes but want it to be written as th: `θ,th`

`filters/regex.txt` is where you can define more complex replacements as regular expressions. I don't actually know how this works, check out genling's documentation or code I guess??