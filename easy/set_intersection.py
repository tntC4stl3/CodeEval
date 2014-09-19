#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(';')
    l1 = set(test[0].split(','))
    l2 = set(test[1].split(','))
    print ','.join(sorted(l1.intersection(l2)))

test_cases.close()