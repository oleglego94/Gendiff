import argparse
from gendiff.diff import generate_diff
from gendiff.formatters import json, plain, stylish


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=['plain', 'json'],
        help='set format of output (default: stylish)',
    )
    args = parser.parse_args()

    if args.format == 'plain':
        args.format = plain.format_plain
    elif args.format == 'json':
        args.format = json.format_json
    else:
        args.format = stylish.format_stylish

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
