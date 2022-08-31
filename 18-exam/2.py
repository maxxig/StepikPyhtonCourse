from functools import reduce
with open('ledger.txt', 'r') as file:
    data = file.readlines()

print(f'${reduce(lambda x, y: x + y, list(map(lambda x: int(x[1:]), data)),0)}')

