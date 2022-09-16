#!/usr/bin/env python3

import argparse


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
    return args
