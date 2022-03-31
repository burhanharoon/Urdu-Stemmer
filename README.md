# Urdu Stemmer
*It is a python based urdu stemmer. From a given list of words, it will try to find their stems using a limited list of affixes given in the program.*

[stemmer.py:](https://github.com/ez-sherlock/Urdu-Stemmer/blob/main/stemmer.py)
This file contains the logic and implementation of the stemmer. It uses regular expressions to find prefixes at the start of a word and suffixes at the end of the word.

> Following are the list of (currently present) affixes:

    urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
	urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']
> To find a prefix it uses this regular expresseion:

`checkPrefix  =  re.search(rf'\A{prefix}', urduWord)`
>To find a suffix it uses this regular expression:

`checkSuffix  =  re.search(rf"{suffix}\Z", urduWord)`
