#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test_list = list(test.strip())
    n = len(test_list)
    test_list = [pow(int(i), n) for i in test_list]
    if sum(test_list) == int(test.strip()):
        print "True"
    else:
        print "False"
test_cases.close()