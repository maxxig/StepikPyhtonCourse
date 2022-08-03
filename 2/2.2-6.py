count = int(input()) #count numbers
mass = []
for i in range(count):
    mass.append(int(input()))
number = int(input()) # number for search
i = 0
j = 0
result = 'НЕТ'
while(i < count):
    j = i + 1
    while(j < count):
        if(mass[i] * mass[j] == number):
            result = 'ДА'
            break
        j += 1
    if result == 'ДА':
        break
    i +=1
print(result)