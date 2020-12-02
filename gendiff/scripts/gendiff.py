from gendiff import cli
from gendiff.generate_diff import generate_diff


def main():
    print(generate_diff(
        cli.args.first_file,
        cli.args.second_file,
        cli.formatter)
    )


if __name__ == '__main__':
    main()
