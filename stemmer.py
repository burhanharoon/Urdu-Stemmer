import re

allUrduAffixes = {}
wrongGuessedStem = {}
totalWords = 0
totalCorrectGuessed = 0

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']


def remove(string):
    return string.replace(" ", "")


#
urduFile = open("urdu-affixes.txt", "r", encoding="utf-8")
for urduWord in urduFile:
    totalWords = totalWords + 1
    x = urduWord.splitlines()
    x = x[0].split('\t\t')
    # Adding real word and its real stem in allUrduAffixes dictionary
    allUrduAffixes[x[0]] = x[1]

for sentence in allUrduAffixes:
    urduWord = sentence
    prefixFound = False

    for prefix in urduPrefixes:
        checkPrefix = re.search(rf'\A{prefix}', urduWord)
        if checkPrefix:
            predictedStem = urduWord[checkPrefix.span(0)[1]:]
            prefixFound = True
            realStem = remove(allUrduAffixes[sentence])
            predictedStem = remove(predictedStem)
            if predictedStem == realStem:
                totalCorrectGuessed = totalCorrectGuessed + 1
            else:
                temp = {
                    "realStem": realStem,
                    "predictedStem": predictedStem,
                }
                wrongGuessedStem[urduWord] = temp
            break

    if not prefixFound:
        for suffix in urduSuffixes:
            checkSuffix = re.search(rf"{suffix}\Z", urduWord)
            if checkSuffix:
                predictedStem = urduWord[:checkSuffix.span(0)[0]]
                # print(predictedStem)
                realStem = remove(allUrduAffixes[sentence])
                predictedStem = remove(predictedStem)
                if predictedStem == realStem:
                    totalCorrectGuessed = totalCorrectGuessed + 1
                else:
                    temp = {
                        "realStem": realStem,
                        "predictedStem": predictedStem,
                    }
                    wrongGuessedStem[urduWord] = temp
                break

print("Total num of words: ", totalWords)
print("Total num of words correctly predicted: ", totalCorrectGuessed)
print("Wrong Words List: ", wrongGuessedStem)
