m = int(input())
res = set()
tmp_set = set()
for i in range(m):
    n = int(input())
    tmp_set.clear()
    for j in range(n):
        tmp_set.add(input())
    if i == 0:
        res = tmp_set.copy()
    else:
        res.intersection_update(tmp_set)
print(*sorted(res), sep='\n')

# m = int(input())
# n = int(input())
# myset = set()
# for i in range(n+m):
#     myset.add(input())
# if len(myset) == (n+m)/2:
#     print('NO')
# else:
#     print((len(myset)) - ((n+m)-len(myset)))



# set1 = set(input().split())
# set2 = set(input().split())
#
# print(*sorted(set1 | set2))


# m = int(input())
# n = int(input())
# setm, setn, setr = set(), set(), set()
# for i in range(m):
#     setm.add(input())
# for i in range(n):
#     setn.add(input())
# setr = setm.symmetric_difference(setn)
# if len(setr)>0:
#     print(len(setr))
# else:
#     print('NO')



# m = int(input())
# n = int(input())
# setm, setn, setr = set(), set(), set()
# for i in range(m):
#     setm.add(input())
# for i in range(n):
#     setn.add(input())
# setr = setm.difference(setn)
# print(len(setr))




# set1 = set(input().split())
# set2 = set(input().split())
#
# if set1 == set2:
#     print('YES')
# else:
#     print('NO')


# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set1 & set2
# set4 = set(int(s) for s in set3)
# if len(set4) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(set4, reverse=True))




# n = int(input())
# m = int(input())
# home = set()
# find_mass = []
# for i in range(n):
#     home.add(input())
#
# for j in range(m):
#     find_mass.append(input())
#
# for f in find_mass:
#     if f in home:
#         print('YES')
#     else:
#         print('NO')



# n = int(input())
# res = set()
# for i in range(n):
#     res.add(input())
# city = input()
# if city in res:
#     print('REPEAT')
# else:
#     print('OK')


# string = input()
# l1 = len(string.split())
# l2 = len(set(string.split()))
# print(l1-l2)


# n,m,k,p = int(input()),int(input()),int(input()),int(input())
# print(n-(m+k-p))


# myset1 = {2, 2, 4, 6, 6}
# r = myset1 *3
# print(r)