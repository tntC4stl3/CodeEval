#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
test_cases = open(sys.argv[1], 'r')
test = test_cases.read().strip()
test = map(int, test.split('\n'))
print sum(test)

test_cases.close()