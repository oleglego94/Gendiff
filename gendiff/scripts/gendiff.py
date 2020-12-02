from gendiff import cli
from gendiff.generate_diff import generate


def main():
    print(generate(
        cli.args.first_file,
        cli.args.second_file,
        cli.formatter)
    )


if __name__ == '__main__':
    main()
