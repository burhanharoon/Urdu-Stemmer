import re

# print(checkWords('بے', 'بےایمان', 'prefix'))
# print(checkWords('بد', 'بدمزاج', 'prefix'))
# print(checkWords('لا', 'لاجواب', 'prefix'))
# print(checkWords('ے', 'بلے', 'prefix'))
# print(checkWords('نا', 'ناخوص', 'prefix'))
# print(checkWords('یاں', 'بلیاں', 'suffix'))
# print(checkWords('وں', 'علاقوں', 'suffix'))
# print(checkWords('دار', 'ایماندار'))

allUrduAffixes = {}

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار']

urduFile = open("urdu-affixes.txt", "r", encoding="utf-8")
for urduWord in urduFile:
    x = urduWord.splitlines()
    x = x[0].split('\t\t')
    allUrduAffixes[x[0]] = x[1]


urduWord = 'ایماندار'
# checkPrefix = re.search('\Aلا', urduWord)
checkSuffix = re.search("دار\Z", urduWord)
if checkSuffix:
    print(urduWord[:checkSuffix.span(0)[0]])
    # print(urduWord[checkPrefix.span(0)[1]:])
