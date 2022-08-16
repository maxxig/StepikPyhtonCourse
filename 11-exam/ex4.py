imput = input().split()
my_dict = dict()

res_string = ''
for s in imput:
    if s in my_dict:
        my_dict[s] += 1
    else:
        my_dict[s] = 1
    res_string = res_string + str(my_dict.get(s)) + ' '
print(res_string.rstrip())
