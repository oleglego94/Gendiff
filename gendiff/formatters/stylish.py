from gendiff.formatters.converting import convert


def parse(item):
    if isinstance(item, list):
        return item[:2]
    return None, item


def create(input, lvl):
    if isinstance(input, dict):
        return render(input, lvl+1)
    return convert(input)


def render(diff_dict, lvl=0):
    result = '{\n'
    tab = '    ' * lvl

    for key, value in diff_dict.items():
        state, data = parse(value)
        content = create(data, lvl)

        if state == 'NESTED':
            result += (tab + '    {}: {}\n'.format(
                key,
                render(data, lvl+1)))

        elif state == 'ADDED':
            result += (tab + '  + {}: {}\n'.format(key, content))

        elif state == 'REMOVED':
            result += (tab + '  - {}: {}\n'.format(key, content))

        elif state == 'CHANGED':
            old_content = content
            new_content = create(value[2], lvl)
            result += (tab + '  - {}: {}\n'.format(key, old_content))
            result += (tab + '  + {}: {}\n'.format(key, new_content))

        else:
            result += (tab + '    {}: {}\n'.format(key, content))

    return ('{}'.format(result) + tab + '}')
