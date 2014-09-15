#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
test_cases = open(sys.argv[1], 'r')
print len(test_cases.read())

test_cases.close()