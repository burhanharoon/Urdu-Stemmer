import re

# print(checkWords('بے', 'بےایمان', 'prefix'))
# print(checkWords('بد', 'بدمزاج', 'prefix'))
# print(checkWords('لا', 'لاجواب', 'prefix'))
# print(checkWords('ے', 'بلے', 'prefix'))
# print(checkWords('نا', 'ناخوص', 'prefix'))
# print(checkWords('یاں', 'بلیاں', 'suffix'))
# print(checkWords('وں', 'علاقوں', 'suffix'))
# print(checkWords('دار', 'ایماندار'))

urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم']
urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار']
urduWord = 'لاجواب'
checkPrefix = re.search('\Aلا', urduWord)
# checkSuffix = re.search("وں\Z", urduWord)
if checkPrefix:
    # print(urduWord[:checkSuffix.span(0)[0]])
    print(urduWord[checkPrefix.span(0)[1]:])
