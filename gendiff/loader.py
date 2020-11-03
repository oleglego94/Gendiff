import json
import yaml


def load_file(file_path):
    file = open(file_path)
    if file_path.endswith('.json'):
        return json.load(file)
    elif file_path.endswith('.yaml'):
        return yaml.safe_load(file)
