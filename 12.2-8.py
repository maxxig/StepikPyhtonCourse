import string
import re
import random
Letters = string.ascii_letters
Letters = re.sub(r'[iIlLoO]','',Letters)
Numbers = str(string.digits)
Numbers = re.sub(r'[01]','',Numbers)
Sym = Letters+Numbers
LettersLower = set(string.ascii_lowercase)
LettersUpper = set(string.ascii_uppercase)
NumberSet = set(Numbers)

def generate_password(length):
    res = ''
    for l in range(length):
        res = res+ Sym[random.randrange(0,len(Sym),1)]
    return res

def generate_passwords(count, length):
    for c in range(count):
        p = generate_password(length)
        while(check_password(p) == False):
            p = generate_password(length)
        print(p)

def check_password(p):
    if len(set(p) & LettersLower)>0 and len(set(p) & LettersUpper) > 0 and len(set(p) & NumberSet) > 0:
        return True
    return False


n, m = int(input()), int(input())
generate_passwords(n, m)