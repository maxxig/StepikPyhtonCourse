import re
with open('file.txt') as file:
    data = file.readlines()
    file.seek(0)
    data1 = file.read()
lines = len(data)
rep = re.compile("[^a-zA-Z, \d, \n]")
rep1 = re.compile("[^a-zA-Z]")

new_data = rep.sub("", data1).replace('\n',' ')
new_data2 = rep1.sub("", data1)
words = len(new_data.split())
symb = len(new_data2)

print(f'Input file contains:\n{symb} letters\n{words} words\n{lines} lines')