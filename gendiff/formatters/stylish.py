from gendiff.formatters.converting import convert


def is_dict(value, lvl):
    if isinstance(value, dict):
        return format_stylish(value, lvl+1)
    return convert(value)


def is_list(value):
    if isinstance(value, list):
        return value[:2]
    return None, value


def format_stylish(diff_dict, lvl=0):
    result = '{\n'
    tab = '    ' * lvl

    for key, value in diff_dict.items():
        state, data = is_list(value)
        content = is_dict(data, lvl)

        if state == 'NESTED':
            result += (tab + '    {}: {}\n'.format(
                key,
                format_stylish(data, lvl+1)))

        elif state == 'ADDED':
            result += (tab + '  + {}: {}\n'.format(key, content))

        elif state == 'REMOVED':
            result += (tab + '  - {}: {}\n'.format(key, content))

        elif state == 'CHANGED':
            old_content = content
            new_content = is_dict(value[2], lvl)
            result += (tab + '  - {}: {}\n'.format(key, old_content))
            result += (tab + '  + {}: {}\n'.format(key, new_content))

        else:
            result += (tab + '    {}: {}\n'.format(key, content))

    return ('{}'.format(result) + tab + '}')
