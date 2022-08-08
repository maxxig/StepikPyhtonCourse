pas = input()
correct_pas = [False, False, False, False] # length. upper, lower, number
if len(pas) >=7:
    correct_pas[0] = True
for p in pas:
    if p.isupper():
        correct_pas[1] = True
    if p.islower():
        correct_pas[2] = True
    if p.isdigit():
        correct_pas[3] = True
if all(correct_pas):
    print('YES')
else:
    print('NO')