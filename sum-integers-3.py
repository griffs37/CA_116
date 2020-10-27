#!/usr/bin/env python

import sys

with open(sys.argv[1], "r") as f:
	a = f.readlines()
	i = 0
	first = 0
	while i < len(a):
		first = first + int(a[i])
		i = i + 1

with open(sys.arv[2], "r") as f:
	a = f.readlines()
	i = 0
	second = 0
	while i < len(a):
		second = second + int(a[i])
		i = i + 1

print first + second
