#!/usr/bin/env python3

from gendiff import cli
from gendiff.gendiff_base import generate_diff


def main():
    cli.parsing_cli()
    diff = generate_diff('tests/json_files/file1.json', 'tests/json_files/file2.json')
    print(diff)


if __name__ == '__main__':
    main()
