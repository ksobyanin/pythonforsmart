#!/bin/python
"""
numerator.py - python-script to display numbered lines of file content

example to use:

$: ./numerator.py file_name

"""

import os
import sys

from utils import numerate_line


if len(sys.argv) < 2:
    print('Filename not specified')
    sys.exit(0)

path_to_file = sys.argv[1]

if os.path.exists(path_to_file):
    with open(path_to_file) as file:

        try:
            lines = file.read().splitlines()

            for i, line in enumerate(lines):
                print(numerate_line(i, line))

        except Exception as error:
            print(error, file=sys.stderr)
            sys.exit(1)

else:
    raise FileNotFoundError(f"File {path_to_file} not found")

