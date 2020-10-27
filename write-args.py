#!/usr/bin/env python

import sys

a = sys.argv[2:]

with open(sys.argv[1], "w") as f:
    i = 0
    while i < len(a):
        f.write(a[i] + "\n")
        i = i + 1
