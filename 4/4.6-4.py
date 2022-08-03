n = input().split()
x,y = int(n[0]), int(n[1])
arr = [[0] * y for _ in range(x)]
counter = 1
for j in range(y):
    for i in range(x):
        arr[i][j] = counter
        counter += 1

for i in range(x):
    for j in range(y):
        print (str(arr[i][j]).ljust(3), end ='')
    print()