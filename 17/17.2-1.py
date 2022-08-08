f = open(input())
file = f.readlines()
f.close()
for s in file:
    print(s.rstrip())
