from functools import reduce
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def get_gema(word):
    w = word.upper()
    gema = reduce(lambda x, y: x+ord(y)-65, list(w), 0)
    return gema
print(*sorted(arr, key=lambda x: (get_gema(x),x)), sep = '\n')

