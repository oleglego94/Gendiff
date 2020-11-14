def format_dict(diff_dict, lvl=0):

    def convert(value):
        if isinstance(value, dict):
            return format_dict(value, lvl+1)
        elif value is False:
            convert_value = 'false'
        elif value is True:
            convert_value = 'true'
        elif value is None:
            convert_value = 'null'
        else:
            convert_value = value
        return convert_value

    result = '{\n'
    tab = '    ' * lvl

    for k, v in diff_dict.items():
        if isinstance(v, tuple):
            state, val = v[:2]
        else:
            state, val = None, v

        if state == 'NESTED':
            result += (tab + '    {}: {}\n'.format(k, format_dict(val, lvl+1)))

        elif state == 'ADDED':
            result += (tab + '  + {}: {}\n'.format(k, convert(val)))

        elif state == 'REMOVED':
            result += (tab + '  - {}: {}\n'.format(k, convert(val)))

        elif state == 'CHANGED':
            result += (tab + '  - {}: {}\n'.format(k, convert(val)))
            result += (tab + '  + {}: {}\n'.format(k, convert(v[2])))

        else:
            result += (tab + '    {}: {}\n'.format(k, convert(val)))

    return ('{}'.format(result) + tab + '}')
