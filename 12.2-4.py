import random
myset = set()
while(len(myset) < 100):
    myset.add(random.randint(1000000,9999999))

{print(i) for i in myset}

# import random
# myset = set()
# tmp = []
# while(len(myset) < 100):
#     tmp.clear()
#     while (len(tmp) < 7):
#         e = random.randrange(0,100,1)
#         if e == 0 and len(tmp) ==0:
#             continue
#         if e not in tmp:
#             tmp.append(str(e))
#     myset.add(tuple(tmp.copy()))
# # for i in myset:
# #     print(*i)
#
# {print(*i) for i in myset}