import os
from gendiff.diff import generate_diff


def test_json_diff():
    file_path1 = os.path.abspath('tests/fixtures/file1.json')
    file_path2 = os.path.abspath('tests/fixtures/file2.json')

    result = '''{
    host: hexlet.io
  - timeout: 50
  + timeout: 20
  - proxy: 123.234.53.22
  - follow: false
  + verbose: true
}'''
    assert generate_diff(file_path1, file_path2) == result
