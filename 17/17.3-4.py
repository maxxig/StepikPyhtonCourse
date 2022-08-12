with open('numbers.txt') as file:
    data = list(map(lambda f: sum(list(map(int,f.rstrip().split()))),file.readlines()))
print(*data, sep='\n')

