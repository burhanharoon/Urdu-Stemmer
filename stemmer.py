import re

# print(checkWords('بے', 'بےایمان', 'prefix'))
# print(checkWords('بد', 'بدمزاج', 'prefix'))
# print(checkWords('لا', 'لاجواب', 'prefix'))
# print(checkWords('ے', 'بلے', 'prefix'))
# print(checkWords('نا', 'ناخوص', 'prefix'))
# print(checkWords('یاں', 'بلیاں', 'suffix'))
# print(checkWords('وں', 'علاقوں', 'suffix'))
# print(checkWords('دار', 'ایماندار'))

urduWord = 'علاقوں'
x = re.search("وں\Z", urduWord)
if x:
    print(urduWord[:x.span(0)[0]])
