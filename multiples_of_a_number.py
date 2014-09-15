#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(' ')
    x = int(test[0])
    n = int(test[1])
    count = 2
    while True:
        result = n * count
        if result >= x:
            print result
            break

test_cases.close()