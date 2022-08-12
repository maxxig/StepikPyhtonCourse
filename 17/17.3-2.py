with open('data.txt') as file:
    data = file.readlines()
print(*[d.rstrip() for d in data[::-1]], sep='\n')