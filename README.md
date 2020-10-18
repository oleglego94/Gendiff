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
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
# gendiff supports JSON files
[![asciicast](https://asciinema.org/a/204dMYi9n5ghZG8DWIbDqnoFg.svg)](https://asciinema.org/a/204dMYi9n5ghZG8DWIbDqnoFg)
# gendiff supports YAML files
[![asciicast](https://asciinema.org/a/tW4NVMdpBdDjULhmNP7yHvzk9.svg)](https://asciinema.org/a/tW4NVMdpBdDjULhmNP7yHvzk9)