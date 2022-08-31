filename = input()
with open(filename, 'r') as file:
    data = list(map(lambda x: x.rstrip(), file.readlines()))

print(*data[-10:], sep = '\n')