#!/usr/bin/env python3

import argparse
from gendiff.gendiff_base import json_to_py


def parsing_cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration\
        files and shows a difference.'
    )
    # Positional arguments:
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Optional arguments:
    parser.add_argument('-f', '--format', help='set format to output')
    args = parser.parse_args()
    if '-h' in args:
        parser.print_help()
    file1 = args['first_file']
    file2 = args['second_file']
    json_to_py(file1, file2)
    
    return args
