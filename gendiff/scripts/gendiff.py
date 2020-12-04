from gendiff.cli import get_parser, RENDERS
from gendiff.diff import generate_diff


def main():
    args = get_parser()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            RENDERS[args.format]
        )
    )


if __name__ == '__main__':
    main()
