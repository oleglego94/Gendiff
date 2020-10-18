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
    union_file = file1.copy()
    union_file.update(file2)
    for k, v in union_file.items():
        if k not in file2:
            result += ('  - {}: {}\n'.format(k, encode(v)))
        elif k not in file1:
            result += ('  + {}: {}\n'.format(k, encode(v)))
        elif file1[k] != file2[k]:
            result += ('  - {}: {}\n'.format(k, encode(file1[k])))
            result += ('  + {}: {}\n'.format(k, encode(file2[k])))
        else:
            result += ('    {}: {}\n'.format(k, encode(v)))
    return ('{{\n{}}}'.format(result))
