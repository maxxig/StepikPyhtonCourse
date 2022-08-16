with open('class_scores.txt', encoding='utf-8') as input_file:
    data = input_file.readlines()

with open('new_scores.txt', 'w', encoding='utf-8') as output_file:
    print(*list(map(lambda x: f'{x.split()[0]} {min(int(x.split()[1].rstrip())+5,100)}', data)), sep='\n', end='', file=output_file)