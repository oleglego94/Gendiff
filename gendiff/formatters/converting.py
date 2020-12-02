def convert(value):
    if value is False:
        convert_value = 'false'
    elif value is True:
        convert_value = 'true'
    elif value is None:
        convert_value = 'null'
    else:
        convert_value = value
    return convert_value
