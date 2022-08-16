cnt_buers = int(input())
dict_result = dict()
for _ in range(cnt_buers):
    buyer = input().split()
    if buyer[0] not in dict_result:
        dict_result[buyer[0]] = {buyer[1]:int(buyer[2])}
    else:
        products = dict_result[buyer[0]]
        if buyer[1] not in products:
            products[buyer[1]] = int(buyer[2])
        else:
            old_value = products[buyer[1]]
            old_value += int(buyer[2])
            products[buyer[1]] = old_value
for k, res in sorted(dict_result.items()):
    print(k,':', sep ='')
    for k2, r in sorted(res.items()):
        print(k2, r)