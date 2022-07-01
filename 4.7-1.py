x = input().split()
n, m = int(x[0]), int(x[1])
arr = []
for i in range(n):
    string = input().split()
    arr.append(string)
input()

arr2 = []
for i in range(n):
    string = input().split()
    arr2.append(string)

for i in range(n):
    for j in range(m):
        print( str(int(arr[i][j])+int(arr2[i][j])).ljust(3), end=' ')
    print()
