#/usr/bin/env python
#coding=utf-8
__author__ = 'jonathan'

import sys

def happy_numbers(num):
    flag = 0
    for i in range(1000):
        next_num = 0
        for item in str(num):
            next_num += pow(int(item), 2)
        num = next_num
        if num == 1:
            flag = 1
            break
    return flag


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print happy_numbers(int(test.strip()))

test_cases.close()