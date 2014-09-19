#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    S, t = test.strip().split(',')
    pos = S.rfind(t)
    print pos

test_cases.close()