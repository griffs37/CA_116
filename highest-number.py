#!/usr/bin/env python

total = 0

i = 0
while i < 6:
	n = input()
	if n > total:
		total = n
	i = i + 1

print total
