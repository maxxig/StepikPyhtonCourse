def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    if (any(filter(lambda x: x in command, ignore))):
        return True
    return False

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('del'))
print(ignore_command('trancate'))