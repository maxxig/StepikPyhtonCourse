def build_query_string(params):
    return '&'.join([f'{k}={v}' for k,v in sorted(params.items())])
print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))