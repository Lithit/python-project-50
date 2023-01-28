import pytest
from gendiff.gendiff_base import generate_diff
import os

def get_path(file_name):
    path_file = os.sep.join(['tests', 'fixtures', file_name])
    return path_file


@pytest.mark.parametrize(
    'file1, file2, expected',
    [('file1.json',
      'file2.json',
      'json_correct_result.txt')]
    )


def test_gendiff_base(file1, file2, expected):
    file1_input = get_path(file1)
    file2_input = get_path(file2)
    path_to_correct_result = get_path(expected)
    with open(path_to_correct_result, 'r') as file:
        correct_result = file.read()
        assert generate_diff(file1_input, file2_input) == correct_result
    



