import random
n = int(input())
all = set()
used_friends = set()
res = set()
for i in range(n):
    all.add(input())

def tryMap(all):
    for a in all:
        a_set = set()
        a_set.add(a)
        can_used = all.difference(a_set).difference(used_friends)
        can_user_arr = list(can_used)
        if len(can_user_arr) == 0:
            return -1
        ind = random.randrange(0,len(can_user_arr),1)
        if (a, can_user_arr[ind]) not in res:
            res.add((a, can_user_arr[ind]))
            used_friends.add(can_user_arr[ind])
    return res

res = tryMap(all)
while(res == -1):
    res = tryMap(all)
for r in res:
    print(r[0],r[1],sep = ' - ')



# import random
# n = int(input())
# all = set()
# res = set()
# for i in range(n):
#     all.add(input())
#
# for a in all:
#     while(1):
#         a_set = set()
#         a_set.add(a)
#         others = all.difference(a_set)
#         others_mass = list(others)
#         if len(others_mass)>0:
#             ind = random.randrange(0,len(others_mass),1)
#             if frozenset({a, others_mass[ind]}) not in res:
#                 res.add(frozenset({a, others_mass[ind]}))
#                 break
# for r in res:
#     print(tuple(r)[0],tuple(r)[1], sep=' - ')


