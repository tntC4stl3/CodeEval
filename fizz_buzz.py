#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys


def fizz_buzz(a, b, n):
    for i in xrange(1, n+1):
        if i % a == 0 and i % b == 0:
            print 'FB',
        elif i % a == 0:
            print 'F',
        elif i % b == 0:
            print 'B',
        else:
            print i,

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(' ')
    test = map(int, test)
    a = test[0]
    b = test[1]
    n = test[2]
    fizz_buzz(a, b, n)
    print ''

test_cases.close()