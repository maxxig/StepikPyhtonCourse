dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
result = dict1.copy()

for key, value in result.items():
    if key in dict2:
       result[key] = result[key] + dict2[key]
for key, value in dict2.items():
    if key not in result:
        result[key] = value


