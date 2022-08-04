import random
import string
def generate_index():
    res =''
    Letters = string.ascii_uppercase
    res = Letters[random.randrange(0,len(Letters),1)]
    res = res + Letters[random.randrange(0, len(Letters), 1)]
    res = res + str(random.randrange(0, 99, 1))
    res = res + '_'
    res = res + str(random.randrange(0, 99, 1))
    res = res + Letters[random.randrange(0, len(Letters), 1)]
    res = res + Letters[random.randrange(0, len(Letters), 1)]
    return res
print(generate_index())