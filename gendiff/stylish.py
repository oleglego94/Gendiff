def format_dict(diff_dict, lvl=0):
    result = '{\n'
    tab = '    ' * lvl

    def encode(value):
        if isinstance(value, dict):
            return format_dict(value, lvl+1)

        if value is False:
            return 'false'
        elif value is True:
            return 'true'
        elif value is None:
            return 'null'
        else:
            return value

    for k, v in diff_dict.items():
        if isinstance(v, tuple):
            state, val = v[:2]
        else:
            state = None
            val = v

        if state == 'NESTED':
            result += (tab + '    {}: {}\n'.format(k, format_dict(val, lvl+1)))

        elif state == 'ADDED':
            result += (tab + '  + {}: {}\n'.format(k, encode(val)))

        elif state == 'REMOVED':
            result += (tab + '  - {}: {}\n'.format(k, encode(val)))

        elif state == 'CHANGED':
            result += (tab + '  - {}: {}\n'.format(k, encode(val)))
            result += (tab + '  + {}: {}\n'.format(k, encode(v[2])))

        else:
            result += (tab + '    {}: {}\n'.format(k, encode(val)))

    return ('{}'.format(result) + tab + '}')
