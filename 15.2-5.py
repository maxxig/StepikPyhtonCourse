def print_products(*args):
    products = [i for i in args if type(i) is str and len(i)>0]
    if len(products) > 0:
        for ind, p in enumerate(products):
            print(f'{ind + 1}) {p}')
    else:
        print('Нет продуктов')
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')