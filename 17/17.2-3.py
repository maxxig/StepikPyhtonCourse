from random import randint
f = open('lines.txt')
data = f.readlines()
f.close()
print(data[randint(0,len(data)-1)])