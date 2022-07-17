import random

length = int(input())
letters = []
pas = ''
for i in range(65,91):
    letters.append(chr(i))
for i in range(97,123):
    letters.append(chr(i))
for i in range(length):
    l = random.randrange(0,len(letters),1)
    pas = pas + letters[l]
print(pas)
