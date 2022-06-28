x = input().split()
n, m = int(x[0]), int(x[1])
array = []
for j in range(n):
    m_array = [i for i in range((j*m+1), ((j+1) * m)+1)]
    if j % 2 == 1:
        m_array.reverse()
        array.append(m_array.copy())
    else:
        array.append(m_array.copy())
    m_array.clear()

for i in range(n):
    for j in range(m):
        print(str(array[i][j]).ljust(3), end=' ')
    print()
