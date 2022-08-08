f = open('numbers.txt')
data = f.readlines()
f.close()
print((int(data[0]) + int(data[1])))