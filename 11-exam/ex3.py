map_cart = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
inp = input()
res = ''
for s in inp:
    res += map_cart[s]
print(res)