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


if __name__ == '__main__':
    count = 0
    sum = 0
    number = 2
    while count < 1000:
        if check_prime(number):
            sum += number
            count += 1
        number +=1
    print sum