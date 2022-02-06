import re

allUrduAffixes = {}

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور']

urduFile = open("urdu-affixes.txt", "r", encoding="utf-8")
for urduWord in urduFile:
    x = urduWord.splitlines()
    x = x[0].split('\t\t')
    allUrduAffixes[x[0]] = x[1]

for sentence in allUrduAffixes:
    urduWord = sentence
    prefixFound = False
    for prefix in urduPrefixes:
        checkPrefix = re.search(rf'\A{prefix}', urduWord)
        if checkPrefix:
            print(urduWord[checkPrefix.span(0)[1]:])
            prefixFound = True
            break
    if not prefixFound:
        for suffix in urduSuffixes:
            checkSuffix = re.search(rf"{suffix}\Z", urduWord)
            if checkSuffix:
                print(urduWord[:checkSuffix.span(0)[0]])
                break

    # # checkPrefix = re.search('\Aلا', urduWord)
    # checkSuffix = re.search("دار\Z", urduWord)
    # if checkSuffix:
    #     print(urduWord[:checkSuffix.span(0)[0]])
    #     # print(urduWord[checkPrefix.span(0)[1]:])
