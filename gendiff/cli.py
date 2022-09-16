#!/usr/bin/env python3

import argparse


def parsing_cli():
    parser = argparse.ArgumentParser(
        descpription='Compares two configuration\
        files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    args = parser.parse.args()
    
    if '-h' in args:
        parser.print_help()