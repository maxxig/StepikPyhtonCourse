import random

s = input()
s_m = []
for i in s:
    s_m.append(i)
random.shuffle(s_m)
print(''.join(s_m))