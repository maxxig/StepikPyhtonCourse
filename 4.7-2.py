x = input().split()
n, m = int(x[0]), int(x[1])
arr = []
for i in range(n):
    string = input().split()
    arr.append(string)
input()
x = input().split()
m, k = int(x[0]), int(x[1])
arr2 = []
for i in range(m):
    string = input().split()
    arr2.append(string)

result_arr = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        summa = 0
        for s in range(m):
            summa += (int(arr[i][s]) * int(arr2[s][j]))
        result_arr[i][j] = summa

for i in range(n):
    for j in range(k):
        print(str(result_arr[i][j]).ljust(3), end=' ')
    print()