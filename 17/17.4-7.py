n = int(input())
for i in range(n):
    with open(input()) as input_file:
        with open('output2.txt','a') as output_file:
            output_file.writelines(input_file.readlines())
            # if i< n-1:
            #     output_file.write('\n')