str = '489 483 43 2 3 84 1 4 3 2 5 4 3 13'
x = str.split()
x2 = x.copy()
for i in range(len(x)-1):
    x[i + 1] = x2[i]
x[0] = x2[len(x)-1]
for i in range(len(x)):
    print(x[i], end=" ")


