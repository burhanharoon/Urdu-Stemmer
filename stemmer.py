def checkWords(affixWord, word, affix):
    if affix == 'suffix':
        wordIndex = len(word) - len(affixWord)
        for char in affixWord:
            if word[wordIndex] == char:
                wordIndex = wordIndex + 1
            else:
                return False
    else:
        wordIndex = 0
        for char in affixWord:
            if word[wordIndex] == char:
                wordIndex = wordIndex + 1
            else:
                return False
    return True


print(checkWords('بے', 'بےایمان', 'prefix'))
print(checkWords('یاں', 'بلیاں', 'suffix'))
print(checkWords('دار', 'ایماندار', 'suffix'))
