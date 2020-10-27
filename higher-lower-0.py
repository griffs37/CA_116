#!/usr/bin/env python

prev = input()

while prev != 0:
	curr = input()
	if prev < curr:
		print "higher"
	elif prev > curr:
	    print "lower"
	else:
		print "equal"
