def pretty_print(data, side = '-', delimiter='|'):
    all_str = f' {delimiter} '.join(map(str, data))
    print(' ' + side * (len(all_str)+2) + ' ')
    print(f'{delimiter} '+ f' {delimiter} '.join(map(str, data)) + f' {delimiter}')
    print(' ' + side * (len(all_str)+2) + ' ')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')