n = int(input())
arr = []
def get_int_adrres(addr):
    a = list(map(int,addr.split('.')))
    return a[0] * 256**3 + a[1] * 256**2 + a[2] * 256 ** 1 + a[3] + 256 ** 0

for _ in range(n):
    arr.append(input())

print(*sorted(arr, key=get_int_adrres), sep='\n')
