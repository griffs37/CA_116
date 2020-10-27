#!/usr/bin/env python

import sys

with open(sys.argv[1], "r") as f:
    a = f.readlines()
    i = 0
    total = 0
    while i < len(a):
        total = total + int(a[i])
        i = i + 1
print total
