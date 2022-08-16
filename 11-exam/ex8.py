cnt_files = int(input())
files_dict = dict()
command_map = {'execute':'X', 'read':'R', 'write':'W'}
for _ in range(cnt_files):
    file = input().split()
    key_d = ''
    value_set = set()
    for i, f in enumerate(file):
        if i == 0:
            key_d = f
        else:
            value_set.add(f)
    files_dict[key_d] = value_set

for _ in range(int(input())):
    file_check = input().split()
    if file_check[1] in files_dict:
        command = command_map[file_check[0]]
        if command in files_dict[file_check[1]]:
            print('OK')
        else:
            print('Access denied')