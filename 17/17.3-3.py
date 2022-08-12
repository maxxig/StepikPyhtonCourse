with open('lines.txt') as file:
    data = list(map(lambda x: x.rstrip(), file.readlines()))
max_value = len(max(data, key=len))
data = filter(lambda x: len(x) == max_value, data)
print(*data, sep = '\n')