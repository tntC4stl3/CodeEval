#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

import math

def check_prime(num):
    for i in xrange(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    else:
        return True

for i in xrange(999, 0, -1):
    num_str = str(i)
    if check_prime(i) and num_str == num_str[::-1]:
        print i
        break
