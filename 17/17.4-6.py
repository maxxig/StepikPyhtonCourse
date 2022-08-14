with open('goats.txt') as input_file:
    data = input_file.readlines()
mode = 0
my_dict = dict()
for i, v in enumerate(data):
    v = v.rstrip()
    if i == 0:
        continue
    if v == 'GOATS':
        mode = 1
        continue
    if mode == 0:
        my_dict[v] = 0
    if mode == 1:
        my_dict[v] += 1

with open('answer.txt', 'w') as output_file:
    print(*list(map(lambda x:f'{x[0]}', list(filter(lambda x:x[1] > sum(my_dict.values()) * 0.07, my_dict.items())))), sep = '\n', end = '', file=output_file)
