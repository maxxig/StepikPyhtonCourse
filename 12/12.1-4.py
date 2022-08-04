import random

myset = set()
while(len(myset) < 7):
    myset.add(random.randrange(1,50,1))
print(*sorted(myset))