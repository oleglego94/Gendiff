import json


def encode(value):
    if value is False:
        return 'false'
    elif value is True:
        return 'true'
    else:
        return value


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    result = ''
    for k, v in file1.items():
        if k not in file2:
            result += ('  - {}: {}\n'.format(k, encode(v)))
        elif file2[k] == v:
            result += ('    {}: {}\n'.format(k, encode(v)))

    for k, v in file2.items():
        if k not in file1:
            result += ('  + {}: {}\n'.format(k, encode(v)))
        elif file1.get(k) != v:
            result += ('  - {}: {}\n'.format(k, encode(file1[k])))
            result += ('  + {}: {}\n'.format(k, encode(v)))

    return ('{{\n{}}}'.format(result))
