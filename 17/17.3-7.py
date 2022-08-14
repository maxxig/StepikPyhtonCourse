import random
with open('first_names.txt') as file_names:
    names = file_names.readlines()
with open('last_names.txt') as file_lastnames:
    lastnames = file_lastnames.readlines()
for i in range(3):
    print(names[random.randint(0, len(names)-1)].rstrip() + ' ' + lastnames[random.randint(0, len(lastnames)-1)].rstrip())