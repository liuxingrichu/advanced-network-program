#!/usr/bin/env python
# -*- coding:utf-8 -*-

def print_err(msg,quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)