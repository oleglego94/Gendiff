from gendiff.cli import args, RENDERS
from gendiff.diff import generate_diff


def main():
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            RENDERS[args.format]
        )
    )


if __name__ == '__main__':
    main()
