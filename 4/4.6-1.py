n = input().split()
x,y = int(n[0]), int(n[1])
print(x, y)
arr = [['.'] * y for _ in range(x)]
is_star = False
for i in range(x):
    for j in range(y):
        if j == 0 and i % 2 == 0:
            is_star = False
        elif j == 0 and i % 2 == 1:
            is_star = True
        if is_star:
            arr[i][j] = '*'
            is_star = False
        else:
            is_star = True

for i in range(x):
    for j in range(y):
        print(arr[i][j], end = ' ')
    print()
#
# for i in range(n):
#     t = input().split()
#     tmp.append(t.copy())
#     t.clear()
# checkSet = set()
# for i in range(n):
#     for j in range(n):
#         if int(tmp[i][j]) > 0:
#             checkSet.add(tmp[i][j])
# if len(checkSet) != n * n:
#     res = 'NO'
# for i in range(n):
#     if sum1 is None:
#         sum1 = sum((int(tmp[i][j])) for j in range(len(tmp[i])))
#     if sum1 != sum((int(tmp[i][j])) for j in range(len(tmp[i]))):
#         res = 'NO'
# for j in range(n):
#     if sum1 != sum((int(tmp[i][j])) for i in range(len(tmp[i]))):
#         res = 'NO'
# if sum1 != sum((int(tmp[i][i])) for i in range(n)):
#     res = 'NO'
# if sum1 != sum((int(tmp[i][n-j-1])) for i in range(n)):
#     res = 'NO'
# print(res)
