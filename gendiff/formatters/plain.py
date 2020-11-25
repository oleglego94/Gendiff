from gendiff.formatters.converting import convert


def is_dict_or_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return "\'{}\'".format(value)
    return convert(value)


def is_list(value):
    if isinstance(value, list):
        return value[:2]
    return None, value


def format_plain(diff_dict, lvl=''):
    result = ''

    for key, value in diff_dict.items():
        state, data = is_list(value)
        content = is_dict_or_str(data)

        if state == 'NESTED':
            result += format_plain(data, lvl+'{}.'.format(key))

        elif state == 'ADDED':
            result += "Property '{}' was added with value: {}\n".format(
                lvl+key,
                content)

        elif state == 'REMOVED':
            result += "Property '{}' was removed\n".format(lvl+key)

        elif state == 'CHANGED':
            old_content = content
            new_content = is_dict_or_str(value[2])
            result += "Property '{}' was updated. From {} to {}\n".format(
                lvl+key,
                old_content,
                new_content)

        else:
            continue

    return result
