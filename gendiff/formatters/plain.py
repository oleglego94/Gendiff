from gendiff.formatters.converting import convert


def parse(item):
    if isinstance(item, list):
        return item[:2]
    return None, item


def create(input):
    if isinstance(input, dict):
        return '[complex value]'
    elif isinstance(input, str):
        return "\'{}\'".format(input)
    return convert(input)


def render(diff_dict, lvl=''):
    result = ''

    for key, value in diff_dict.items():
        state, data = parse(value)
        content = create(data)

        if state == 'NESTED':
            result += render(data, lvl+'{}.'.format(key))

        elif state == 'ADDED':
            result += "Property '{}' was added with value: {}\n".format(
                lvl+key,
                content)

        elif state == 'REMOVED':
            result += "Property '{}' was removed\n".format(lvl+key)

        elif state == 'CHANGED':
            old_content = content
            new_content = create(value[2])
            result += "Property '{}' was updated. From {} to {}\n".format(
                lvl+key,
                old_content,
                new_content)

        else:
            continue

    return result
