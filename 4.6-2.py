n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            arr[i][j] = 1
        if i > n - j - 1:
            arr[i][j] = 2

for i in range(n):
    for j in range(n):
        print (arr[i][j], end =' ')
    print()