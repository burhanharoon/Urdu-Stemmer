import re

allUrduAffixes = {}
wrongGuessedStem = {}
totalWords = 0
totalCorrectGuessed = 0

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']

# Removes space form a urdu word 
def remove(string):
    return string.replace(" ", "")

# Opening the file which contains all urdu words and their respective stems
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
    foundBothPrefixSuffix = False
    
    # Checks if both prefix and suffix are present in a word
    # But right now it's out of this program's scope
    # Feel free to use in your projects if required!
    # for prefix in urduPrefixes:
    #     for suffix in urduSuffixes:
    #         checkPrefix = re.search(rf'\A{prefix}', urduWord)
    #         checkSuffix = re.search(rf"{suffix}\Z", urduWord)
    #         if checkPrefix and checkSuffix:
    #             foundBothPrefixSuffix = True
    #             print(checkPrefix,checkSuffix)

    if not foundBothPrefixSuffix:
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
print("Fitness Percentage: ", totalCorrectGuessed / totalWords * 100)
