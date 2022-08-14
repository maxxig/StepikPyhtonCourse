import random
res = [random.randint(111,777) for i in range(25)]
with open('random.txt', 'w') as output_file:
     print(*res, sep='\n', file=output_file)