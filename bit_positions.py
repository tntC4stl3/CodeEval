#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(',')
    n, p1, p2 = map(int, test)
    n_bin = bin(n)[2:]
    p1 *= -1
    p2 *= -1
    if n_bin[p1] == n_bin[p2]:
        print 'true'
    else:
        print 'false'
test_cases.close()