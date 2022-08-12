f = open('prices.txt', encoding='utf-8')
data = f.readlines()
f.close()
sum = 0
for d in data:
    d_s = d.rstrip().split('\t')
    sum += int(d_s[1]) * int(d_s[2])
print(sum)