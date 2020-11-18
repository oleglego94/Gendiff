def convert(value):
    if isinstance(value, dict):
        convert_value = '[complex value]'
    elif isinstance(value, str):
        convert_value = "\'{}\'".format(value)
    elif value is False:
        convert_value = 'false'
    elif value is True:
        convert_value = 'true'
    elif value is None:
        convert_value = 'null'
    else:
        convert_value = value
    return convert_value


def format_plain(diff_dict, key=''):
    result = ''
    for k, v in diff_dict.items():
        if isinstance(v, tuple):
            state, val = v[:2]
        else:
            state, val = None, v

        if state == 'NESTED':
            result += format_plain(val, key+'{}.'.format(k))

        elif state == 'ADDED':
            result += "Property '{}' was added with value: {}\n".format(key+k, convert(val))  # noqa: E501

        elif state == 'REMOVED':
            result += "Property '{}' was removed\n".format(key+k)

        elif state == 'CHANGED':
            result += "Property '{}' was updated. From {} to {}\n".format(key+k, convert(val), convert(v[2]))  # noqa: E501

        else:
            continue

    return result
