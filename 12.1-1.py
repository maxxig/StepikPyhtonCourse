import random

n = int(input())    # количество попыток

for i in range(n):
    if random.randrange(0,2,1) == 0:
        print('Орел')
    else:
        print('Решка ')