s = input().split()
s_map = map(lambda x: 255-int(x),s)
print(*s_map)
