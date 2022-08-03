str = 'Р'
count, max_count = 1, 0
if 'Р' in str:
    max_count = 1
for i in range(len(str) - 1):
    if str[i + 1] == str[i] and str[i + 1] == "Р":
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1
print(max_count)
