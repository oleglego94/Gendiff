def encode(value):
    if value is False:
        return 'false'
    elif value is True:
        return 'true'
    else:
        return value
