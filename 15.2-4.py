def greet(name, *args):
    #return f'Hello, {name}' + f'{" and " if len(args)>0 else ""}' +' and '.join(args) +'!'
    return f'Hello, {name}{" and " if len(args) > 0 else ""}{" and ".join(args)}!'
print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))