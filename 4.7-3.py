n = int(input())
arr, result = [], []
for i in range(n):
    string = input().split()
    arr.append(string)
x = int(input())

result = arr.copy()


def mult_two_arrays(arr1, arr2,n):
    result_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            summa = 0
            for s in range(n):
                summa += (int(arr1[i][s]) * int(arr2[s][j]))
            result_arr[i][j] = summa
    return result_arr


for s in range(x-1):
    result = mult_two_arrays(result, arr,n)

for i in range(n):
    for j in range(n):
        print(str(result[i][j]).ljust(3), end=' ')
    print()