func = lambda x: True if str(x).lower()[0] == 'a' and str(x).lower()[-1] == 'a' else False
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))