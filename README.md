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

[urdu-affixes.txt](https://github.com/ez-sherlock/Urdu-Stemmer/blob/main/urdu-affixes.txt):
This file contains the input words for the **stemmer.py**. It contains two colloums and are read from urdu way of reading files (right to left).


![words](https://user-images.githubusercontent.com/89704304/161375582-f42a2447-496e-499d-a9d3-002b58bb0dee.PNG)


 - The words on the most right act as a input for the program. The stemmer reads them and finds their stems.
 - The words on the most left are the actual stem words of words on the right side. These are wriiten manuually to calcaulate the efficency/accuracy of the program i.e. How many stem words the program calculated right?
