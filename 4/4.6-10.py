x = input().split()
n, m = int(x[0]), int(x[1])
arr = [[0] * m for _ in range(n)]

z = 1
top_line_max = m
righ_line_max = n
bottom_line_max = m-1
left_line_max = n-1
spiral_lvl = 0
while z <= n*m:
    for i in range(spiral_lvl,top_line_max):
        arr[spiral_lvl][i] = z
        z += 1
    for i in range(spiral_lvl+1,righ_line_max):
        arr[i][top_line_max-1] = z
        z += 1
    if (righ_line_max-1) > spiral_lvl:
        for i in range(bottom_line_max-1,spiral_lvl-1,-1):
            arr[righ_line_max-1][i] = z
            z += 1
    if spiral_lvl < top_line_max-1:
        for i in range(left_line_max-1,spiral_lvl,-1):
            arr[i][spiral_lvl] = z
            z += 1
    spiral_lvl += 1
    top_line_max -= 1
    righ_line_max -= 1
    bottom_line_max -=1
    left_line_max -=1
for i in range(n):
    for j in range(m):
        print(str(arr[i][j]).ljust(3), end=' ')
    print()