import json
import yaml


def parse(path, data):
    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(data)
    return json.load(data)


def load(file_path):
    with open(file_path) as file:
        return parse(file_path, file)
