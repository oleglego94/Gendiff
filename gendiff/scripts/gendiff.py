import argparse
from gendiff.diff import generate_diff
from gendiff.stylish import format_stylish


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        default=format_stylish,
        help='set format of output (default: stylish format)',
    )
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
