#!/usr/bin/env python3

from gendiff.cli import parsing_cli
from gendiff.gendiff_base import generate_diff


def main():
    args = parsing_cli()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
