n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = abs(i-j)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end =' ')
    print()




# xy = input()
# x = '87654321'.index(xy[1])
# y = 'abcdefgh'.index(xy[0])
# arr = [['.'] * 8 for _ in range(8)]
#
# for i in range(8):
#     arr[x][i] = '*'
#     arr[i][y] = '*'
# i,j = 0,0
# for i in range(8):
#     for j in range(8):
#         if(abs(i-x) == abs(j-y)):
#             arr[i][j] = '*'
#
# arr[x][y] = 'Q'
#
# for i in range(8):
#     for j in range(8):
#         print(arr[i][j], end =' ')
#     print()




# n = int(input())
# result_list = []
# check_set = set(range(1,n+1))
# result = 'YES'
#
# for i in range(n):
#     t = input().split()
#     result_list.append(t.copy())
#     t.clear()
#
# for i2 in range(n):
#     for j2 in range(n):
#         result_list[i2][j2] = int(result_list[i2][j2])
#
# for j in range(n):
#     if check_set != set(result_list[j]):
#         result = 'NO'
#         break
#     if result == 'NO':
#         break
# i,j = 0,0
# check = []
# for j in range(n):
#     for i in range(n):
#         check.append(result_list[i][j])
#     if check_set != set(check):
#         result = 'NO'
#         break
#     check.clear()
#
# print(result)

# n = int(input())
# result_list = []
# result = 'YES'
# for i in range(n):
#     t = input().split()
#     result_list.append(t.copy())
#     t.clear()
# for i in range(n):
#     for j in range(n):
#         if result_list[i][j] != result_list[n-1-j][n-1-i]:
#             result = 'NO'
#
# print(result)


# n = int(input())
# arr = [['.'] * n for _ in range(n)]
#
# for i in range(n):
#     arr[i][i] = '*'
#     arr[i][n - 1 - i] = '*'
#     arr[i][(n // 2)] = '*'
#     arr[(n // 2)][i] = '*'
#
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end =' ')
#     print()

# n = int(input())
# result_list = []
# for i in range(n):
#     t = input().split()
#     result_list.append(t.copy())
#     t.clear()
# result_list2 = [[0]*n for x in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         result_list2[j][i] = result_list[i][j]
#
# for i in range(n):
#     for j in range(n):
#         print(result_list2[i][j], end =' ')
#     print()


# n = int(input())
# result_list = []
#
# for i in range(n):
#     t = input().split()
#     result_list.append(t.copy())
#     t.clear()
# max = int(result_list[n-1][n-1])
# for i in range(n):
#     for j in range(n):
#         if ((i>=j and i >= n-1-j) or (i<=j and i>=n-1-j)) and int(result_list[i][j]) > max:
#             max = int(result_list[i][j])
# print(max)

# string = input().split()
# n = int(input())
# arr = [[] for x in range(n)]
# i, j = 0,0
# while(i<len(string)):
#     arr[j].append(string[i])
#     i += 1
#     j += 1
#     if j >= n:
#         j = 0
# print(arr)