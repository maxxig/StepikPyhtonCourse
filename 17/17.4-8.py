import datetime
with open('logfile.txt', encoding='utf-8') as input_file:
    data = input_file.readlines()

output_data = list(filter(lambda x:(datetime.datetime.strptime(x.split(', ')[2].rstrip(),'%H:%M') - datetime.datetime.strptime(x.split(', ')[1],'%H:%M')) >= datetime.timedelta(seconds=3600), data))
output_data = list(map(lambda x: x.split(', ')[0], output_data))

with open('output3.txt', 'w', encoding='utf-8') as output_file:
    print(*output_data, sep='\n', file=output_file)
# for d in data:
#     s = d.split(', ')
#     u = s[0]
#     ds = s[1]
#     df = s[2].rstrip()
#     diff = (datetime.datetime.strptime(df,'%H:%M') - datetime.datetime.strptime(ds,'%H:%M')) > datetime.timedelta(seconds=3600)
#     print(diff)