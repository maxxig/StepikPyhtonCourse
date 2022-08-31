with open('words.txt', 'r') as file:
    data = file.read().split()

result = list(filter(lambda x: len(x) == len(max(data, key=len)), data))
print(*result, sep = '\n')