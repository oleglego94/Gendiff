from os.path import abspath
from gendiff import diff
from gendiff.formatters import stylish, plain, json


def test_generate_diff():
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
    json_diff = open(abspath('tests/fixtures/json_diff.json')).read()

    assert diff.generate_diff(
        json_before,
        json_after,
        stylish.render) == simple_diff
    assert diff.generate_diff(
        yaml_before,
        yaml_after,
        stylish.render) == simple_diff

    assert diff.generate_diff(
        complex_json_before,
        complex_json_after,
        stylish.render) == stylish_diff
    assert diff.generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        stylish.render) == stylish_diff

    assert diff.generate_diff(
        complex_json_before,
        complex_json_after,
        plain.render) == plain_diff
    assert diff.generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        plain.render) == plain_diff

    assert diff.generate_diff(
        complex_json_before,
        complex_json_after,
        json.render) == json_diff
    assert diff.generate_diff(
        complex_yaml_before,
        complex_yaml_after,
        json.render) == json_diff
