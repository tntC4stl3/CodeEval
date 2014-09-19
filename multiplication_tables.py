#!/usr/bin/env python
# coding: utf-8

__author__ = 'jonathan'

base = range(1, 13)

for i in xrange(1, 13):
    row = ['%4d' % (item * i) for item in base]
    print ''.join(row)