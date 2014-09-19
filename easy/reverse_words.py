#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(' ')
    print ' '.join(reversed(test))

test_cases.close()