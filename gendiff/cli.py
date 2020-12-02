import argparse
from gendiff.formatters import json, plain, stylish


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    choices=['plain', 'json', 'stylish'],
    help='set format of output (default: stylish)',
)
args = parser.parse_args()

if args.format == 'plain':
    formatter = plain.render
elif args.format == 'json':
    formatter = json.render
else:
    formatter = stylish.render
