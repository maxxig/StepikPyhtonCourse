import re
with open('nums.txt') as file:
    data = file.read()
rep = re.compile("[^\d]")
new_data = rep.sub(" ", data)
result = sum(list(map(int,  new_data.split())))
print(result)

