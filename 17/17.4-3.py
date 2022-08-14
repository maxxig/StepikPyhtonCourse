with open('input.txt') as input_file:
    data = input_file.readlines()
with open('output.txt', 'w') as output_file:
    output_file.writelines([f'{i}) {v}' for i, v in enumerate(data, start=1)])
