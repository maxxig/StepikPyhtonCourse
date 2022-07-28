str = input()
m  =[i for i in str.split()]

def mysort(val):
    sum =0
    for v in val:
        sum += int(v)
    return sum

m = sorted(m, key=lambda x: (mysort(x), int(x)))
print(*m)



# str = input()
# m  =[i for i in str.split()]
#
# def mysort(val):
#     sum =0
#     for v in val:
#         sum += int(v)
#     return sum
# m = sorted(m, key=mysort)
# print(*m)