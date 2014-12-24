#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test_list = re.split('\s+', test.strip())
    test_list = [word[0].capitalize() + word[1:] for word in test_list]
    print ' '.join(test_list)
test_cases.close()