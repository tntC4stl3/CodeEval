#/usr/bin/env python
#coding=utf-8
__author__ = 'jonathan'

import sys

def swap_case(string):
    return string.swapcase()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print swap_case(test.strip())

test_cases.close()