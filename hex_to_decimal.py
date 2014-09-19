#/usr/bin/env python
#coding=utf-8
__author__ = 'jonathan'

import sys

def hex_to_decimal(string):
    return int(string, 16)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print hex_to_decimal(test.strip())

test_cases.close()