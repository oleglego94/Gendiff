from os.path import abspath
from gendiff.diff import generate_diff
from gendiff.stylish import format_stylish


def test_diff():
    json_before = abspath('tests/fixtures/before.json')
    json_after = abspath('tests/fixtures/after.json')
    complex_json_before = abspath('tests/fixtures/complex_before.json')
    complex_json_after = abspath('tests/fixtures/complex_after.json')

    yaml_before = abspath('tests/fixtures/before.yaml')
    yaml_after = abspath('tests/fixtures/after.yaml')
    complex_yaml_before = abspath('tests/fixtures/complex_before.yaml')
    complex_yaml_after = abspath('tests/fixtures/complex_after.yaml')

    result = open(abspath('tests/fixtures/result.txt')).read()
    complex_result = open(abspath('tests/fixtures/complex_result.txt')).read()

    assert generate_diff(json_before, json_after, format_stylish) == result
    assert generate_diff(yaml_before, yaml_after, format_stylish) == result
    assert generate_diff(
        complex_json_before,
        complex_json_after,
        format_stylish) == complex_result
    assert generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        format_stylish) == complex_result
