#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test.strip())
    a = fib()
    for i in xrange(test):
        a.next()
    print a.next()

test_cases.close()