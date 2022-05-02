from io import TextIOWrapper

def my_open(filename, mode):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if lines[0] == '[busy]\n':
        return 0

    lines[0] = '[busy]\n'

    with open(filename, 'w') as out:
        out.writelines(lines)

    return open(filename, mode)

def my_close(file):
    if not file:
        return
    file = TextIOWrapper(file)
    name = file.name
    file.close()

    with open(name, 'r') as out:
        lines = out.readlines()
    
    lines[0] = '[free]\n'
    with open(name, 'w') as out:
        out.writelines(lines)
    
def set_free(filename):
    with open(filename, 'r') as out:
        lines = out.readlines()
    if (lines[0] == '[free]\n') or (lines[0] == '[busy]\n'):
        lines[0] = '[free]\n'
    else:
        lines.insert(0, '[free]\n')
    with open(filename, 'w') as out:
        out.writelines(lines)
