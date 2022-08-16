def merge(values):
    res_dict = dict()
    for v in values:
        for k,v in v.items():
            if k not in res_dict:
                res_dict[k] = {v,}
            else:
                ss = res_dict[k]
                ss.add(v)
                res_dict[k] = ss
    return res_dict
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)