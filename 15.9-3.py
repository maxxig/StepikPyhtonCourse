abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))

res = []
# print(list(abscissas))
# print(list(ordinates))
# print(list(applicates))
for x,y,z in zip(abscissas, ordinates, applicates):
    if x**2+y**2+z**2 <= 4:
        res.append(True)
    else:
        res.append(False)
print(all(res))