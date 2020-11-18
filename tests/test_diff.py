from os.path import abspath
from gendiff.diff import generate_diff
from gendiff.formatters import stylish, plain


def test_diff():
    json_before = abspath('tests/fixtures/before.json')
    json_after = abspath('tests/fixtures/after.json')
    complex_json_before = abspath('tests/fixtures/complex_before.json')
    complex_json_after = abspath('tests/fixtures/complex_after.json')

    yaml_before = abspath('tests/fixtures/before.yaml')
    yaml_after = abspath('tests/fixtures/after.yaml')
    complex_yaml_before = abspath('tests/fixtures/complex_before.yaml')
    complex_yaml_after = abspath('tests/fixtures/complex_after.yaml')

    simple_diff = open(abspath('tests/fixtures/simple_diff.txt')).read()
    stylish_diff = open(abspath('tests/fixtures/stylish_diff.txt')).read()
    plain_diff = open(abspath('tests/fixtures/plain_diff.txt')).read()

    assert generate_diff(json_before, json_after, stylish.format_stylish) == simple_diff  # noqa: E501
    assert generate_diff(yaml_before, yaml_after, stylish.format_stylish) == simple_diff  # noqa: E501
    assert generate_diff(
        complex_json_before,
        complex_json_after,
        stylish.format_stylish) == stylish_diff
    assert generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        stylish.format_stylish) == stylish_diff
    assert generate_diff(
        complex_json_before,
        complex_json_after,
        plain.format_plain) == plain_diff
    assert generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        plain.format_plain) == plain_diff
