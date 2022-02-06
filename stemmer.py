import re

allUrduAffixes = {}
totalWords = 0
totalCorrectGuessed = 0

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']


def remove(string):
    return string.replace(" ", "")


urduFile = open("urdu-affixes.txt", "r", encoding="utf-8")
for urduWord in urduFile:
    totalWords = totalWords + 1
    x = urduWord.splitlines()
    x = x[0].split('\t\t')
    allUrduAffixes[x[0]] = x[1]

for sentence in allUrduAffixes:
    urduWord = sentence
    prefixFound = False

    for prefix in urduPrefixes:
        checkPrefix = re.search(rf'\A{prefix}', urduWord)
        if checkPrefix:
            predictedStem = urduWord[checkPrefix.span(0)[1]:]
            # print(predictedStem)
            prefixFound = True
            realStem = remove(allUrduAffixes[sentence])
            predictedStem = remove(predictedStem)
            if predictedStem == realStem:
                totalCorrectGuessed = totalCorrectGuessed + 1
            # else:
            #     print(realStem, predictedStem)
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
                # else:
                #     print(realStem, predictedStem)
                break

print(totalWords)
print(totalCorrectGuessed)
