with open('text.txt') as file:
    data = file.readline()
print(data[::-1])