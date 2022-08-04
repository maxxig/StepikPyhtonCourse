import random
my = []
mass = [[0]*5 for i in range(5)]

while(len(my)<24):
    val = random.randrange(1,76,1)
    if val not in my:
        my.append(val)

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            mass[i][j] = 0
        else:
            mass[i][j] = my.pop()
for i in range(5):
    for j in range(5):
        print(str(mass[i][j]).ljust(3), end=' ')
    print()
