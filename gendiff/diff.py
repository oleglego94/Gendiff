from collections import OrderedDict
from gendiff.loader import load_file
from gendiff.stylish import format_dict


def build_diff_dict(dict_before, dict_after):
    diff = {}

    before_keys = set(dict_before.keys())
    after_keys = set(dict_after.keys())

    added_keys = after_keys - before_keys
    for k in added_keys:
        diff[k] = ('ADDED', dict_after[k])

    removed_keys = before_keys - after_keys
    for k in removed_keys:
        diff[k] = ('REMOVED', dict_before[k])

    common_keys = before_keys & after_keys
    for k in common_keys:
        old_v = dict_before[k]
        new_v = dict_after[k]
        if isinstance(old_v, dict) and isinstance(new_v, dict):
            diff[k] = ('NESTED', build_diff_dict(old_v, new_v))
        elif old_v != new_v:
            diff[k] = ('CHANGED', old_v, new_v)
        else:
            diff[k] = ('UNCHANGED', old_v)

    return OrderedDict(sorted(diff.items()))


def generate_diff(file_path_before, file_path_after):
    before_dict = load_file(file_path_before)
    after_dict = load_file(file_path_after)
    diff_dict = build_diff_dict(before_dict, after_dict)
    return format_dict(diff_dict)
