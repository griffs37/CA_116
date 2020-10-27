#!/usr/bin/env python

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

a = sys.stdin.read().split()


i = 0
while i < len(a):
	if a[i] in fruit:
		print a[i]
	i = i + 1