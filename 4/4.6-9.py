x = input().split()
n, m = int(x[0]), int(x[1])
arr = [[0] * m for _ in range(n)]

z,index = 1,0
while z <= n*m:
    for i in range(n):
        for j in range(m):
            if i + j == index:
                arr[i][j] = z
                z += 1
                continue
    index +=1

for i in range(n):
    for j in range(m):
        print(str(arr[i][j]).ljust(3), end=' ')
    print()