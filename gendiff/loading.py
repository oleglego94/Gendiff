import json
import yaml


def load(file_path):
    with open(file_path) as file:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        return json.load(file)
