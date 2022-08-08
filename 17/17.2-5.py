f = open('nums.txt')
data = f.read().split()
f.close()
print(int(data[0])+int(data[1]))