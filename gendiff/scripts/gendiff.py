from gendiff import cli
from gendiff.diff import generate_diff


def main():
    print(generate_diff(
        cli.args.first_file,
        cli.args.second_file,
        cli.renders[cli.args.format])
    )


if __name__ == '__main__':
    main()
