x = input().split()
n, m = int(x[0]), int(x[1])
array = []
m_array = [i+1 for i in range(m)]

for i in range(n):
    array.append(m_array.copy())
    m_array.append(m_array.pop(0))

for i in range(n):
    for j in range(m):
        print (array[i][j], end =' ')
    print()