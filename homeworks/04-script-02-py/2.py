#!/usr/bin/env python3

import os
import sys


if len(sys.argv) > 1:
    curr_dir = sys.argv[1]
    result_os = os.popen(f'cd {curr_dir} && git status').read()
else:
    curr_dir = os.popen('cd').read().strip()
    result_os = os.popen('git status').read()


if result_os.find('not a git repository') == -1:
    for result in result_os.split('\n'):
        if result.find('modified') != -1 or result.find('new file') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(curr_dir + "\\" + prepare_result)
else:
    print('Указанный путь не является Git репозиторием!')