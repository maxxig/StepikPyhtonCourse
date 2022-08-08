n = int(input())
classes = dict()
for i in range(n):
    k = int(input())
    grades = []
    for j in range(k):
        student = input().split()
        grades.append(int(student[1]))
    classes[i] = grades.copy()
    grades.clear()

print(f'{"YES" if all(map(lambda x: True if 5 in x else False, classes.values())) == True else "NO"}')