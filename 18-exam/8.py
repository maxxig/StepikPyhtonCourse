filename = input()
with open(filename, 'r') as file:
    data = file.readlines()
is_found = 0
for i,d in enumerate(data):
    if d.startswith('def') and not data[i-1].startswith('#'):
        print(d[4:d.find("(")].rstrip())
        is_found = 1
if is_found == 0:
    print('Best Programming Team')
