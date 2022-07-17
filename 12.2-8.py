import string
import re
import random
Letters = string.ascii_letters
Letters = re.sub(r'[iIlLoO]','',Letters)
Numbers = str(string.digits)
Numbers = re.sub(r'[01]','',Numbers)
Sym = Letters+Numbers

def generate_password(length):
    res = ''
    for l in range(length):
        res = res+ Sym[random.randrange(0,len(Sym),1)]
    print(res)

def generate_passwords(count, length):
    for c in range(count):
        generate_password(length)

n, m = int(input()), int(input())
generate_passwords(n, m)