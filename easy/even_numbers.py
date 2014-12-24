#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys

test_cases = open(sys.argv[1], 'r')
for num in test_cases:
    num = int(num.strip())
    if num % 2 == 1:
        print 0
    else:
        print 1
test_cases.close()