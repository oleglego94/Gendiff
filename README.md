# python-project-lvl2
![Python CI](https://github.com/oleglego94/python-project-lvl2/workflows/Python%20CI/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/ee4b89fc17de5b826ef0/maintainability)](https://codeclimate.com/github/oleglego94/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ee4b89fc17de5b826ef0/test_coverage)](https://codeclimate.com/github/oleglego94/python-project-lvl2/test_coverage)
### Hexlet tests and linter status:
![Actions Status](/workflows/hexlet-check/badge.svg)
## Description
Gendiff is a CLI-utility defining the difference between two files.
## Installation
"gendiff" requires Python 3.6+ to run.
```
$ pip install -i https://test.pypi.org/simple/ oleglego94-gendiff --extra-index-url https://pypi.org/simple/
```
## Usage
```
$ gendiff -h
usage: gendiff [-h] [-f {plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {plain,json}, --format {plain,json}
                        set format of output (default: stylish format)
```
# gendiff for JSON files in stylish format
[![asciicast](https://asciinema.org/a/iAYE4MoFdnAVWocCNeCdO17Zk.svg)](https://asciinema.org/a/iAYE4MoFdnAVWocCNeCdO17Zk)
# gendiff for YAML files in stylish format
[![asciicast](https://asciinema.org/a/j31Ji1cUoaiLBFJQqSm0yfjE5.svg)](https://asciinema.org/a/j31Ji1cUoaiLBFJQqSm0yfjE5)
# gendiff for JSON tree files in stylish format
[![asciicast](https://asciinema.org/a/7dXLOWSRIsanxHujLq9W96o7u.svg)](https://asciinema.org/a/7dXLOWSRIsanxHujLq9W96o7u)
# gendiff for YAML tree files in stylish format
[![asciicast](https://asciinema.org/a/aXJWgsrs4x26QonyKEGLIFOXl.svg)](https://asciinema.org/a/aXJWgsrs4x26QonyKEGLIFOXl)
# gendiff for JSON, YAML files in plain format
[![asciicast](https://asciinema.org/a/N3uIQTU5x1u7xUUlqVfaf04xz.svg)](https://asciinema.org/a/N3uIQTU5x1u7xUUlqVfaf04xz)
# gendiff for JSON, YAML files in JSON format
[![asciicast](https://asciinema.org/a/rwFLn9v3zFyZZVc0l6VnqSIu9.svg)](https://asciinema.org/a/rwFLn9v3zFyZZVc0l6VnqSIu9)