count = int(input())
result_list = {}
result_for_print = ''
for i in range(count):
    result_list.update({i: input()})


def search_function(find_string):
    letter_a = find_string.find('a')
    letter_n = find_string.find('n', letter_a)
    letter_t = find_string.find('t', letter_n)
    letter_o = find_string.find('o', letter_t)
    letter_2n = find_string.find('n', letter_o)
    # if letter_n > 0:
    #     letter_2n = find_string.find('n', letter_n + 1)
    if letter_2n > letter_o and letter_o > letter_t and letter_t > letter_n and letter_n > letter_a and letter_a >= 0:
        return True
    return False


for j in range(len(result_list)):
    if search_function(result_list.get(j)) == True:
        if len(result_for_print) ==0:
            result_for_print = (j+1).__str__()
        else:
            result_for_print = result_for_print + ' ' + (j+1).__str__()

print(result_for_print)