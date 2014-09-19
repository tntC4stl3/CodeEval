#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    l1 = test.strip().split(',')
    l2 = sorted(set(l1), key=l1.index)
    print ','.join(l2)

test_cases.close()