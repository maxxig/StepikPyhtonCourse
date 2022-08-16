def read_csv():
    with open('data.csv') as file:
        data = file.readlines()
    keys, res = [], []
    for k, v in enumerate(data):
        if k == 0:
            keys = [d.rstrip() for d in data[0].split(',')]
        else:
            res.append(dict(zip(keys, [d.rstrip() for d in v.split(',')])))
    return res
read_csv()