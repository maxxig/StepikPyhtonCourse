with open('population.txt') as file:
    data = file.readlines()

convert_data = filter(lambda x: int(x.split('\t')[1].rstrip())>500000 and x.split('\t')[0][0] == 'G', data)

print(*list(map(lambda x: x.split('\t')[0], list(convert_data))), sep='\n')