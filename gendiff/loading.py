import json
import yaml


def load_file(file_path):
    file = open(file_path)
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return yaml.safe_load(file)
    return json.load(file)
