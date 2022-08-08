a = int(input())
b = int(input())

arr = [n for n in range(a, b+1) if '0' not in str(n)]

def func(x):
    for s in str(x):
        if x % int(s) != 0:
            return False
    return True

print(*list(filter(func, arr)))