with open('grades.txt', 'r')  as file:
    data = file.readlines()
counter = 0
for d in data:
    current_student = 0
    for i, s in enumerate(d.split()):
        if i == 0:
            continue
        else:
            if int(s)>=65:
                current_student +=1
    if current_student == 3:
        counter += 1
print(counter)