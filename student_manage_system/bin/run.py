#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import platform

if platform.system() == 'Windows':
    BASE_DIR = "\\".join(
        os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__))
                        ).split('/')[:-1]

sys.path.insert(0, BASE_DIR)

from modules import actions


def main():
    obj = actions.Action()
    obj.func()


if __name__ == '__main__':
    main()
