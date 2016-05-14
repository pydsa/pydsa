# !/usr/bin/env python
'''
This module automatically checks for pep8 format.
It scans the complete folder, searches for python files
(ignoring the virtual environment python files) and automatially
format it according to pep8 format using a python plugin 'autopep8'.
'''

import os
import autopep8
import sys


BASE_DIR = os.path.abspath(__file__)


def format_file(path):
    '''
    The function, using 'for' loop scans all the directories as well
    as sub-directories of the folder for python file and checks
    for pep8 format.
    '''
    p = ""
    for dirpath, _, filenames in os.walk(path):
        if(os.path.exists(os.path.join(dirpath, 'bin/activate'))):
            p = dirpath
        for f in filenames:
            if f.endswith('.py'):
                filename = os.path.abspath(os.path.join(dirpath, f))
                if (not bool(p)):
                    if os.access(filename, os.W_OK):
                        try:
                            file1 = open(filename, 'r')
                            source_code = file1.read()
                            file1.seek(0)
                            file1 = open(filename, 'w')
                            file1.truncate()
                            file1.write(autopep8.fix_code(source_code))
                            file1.close()
                        except:
                            print(filename)
                            print(sys.exc_info()[0])


if __name__ == "__main__":
    path_of_dir = [
        os.path.dirname(BASE_DIR),
    ]
    for x in path_of_dir:
        format_file(x)
