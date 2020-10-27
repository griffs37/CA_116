#!usr/bin/env python

a = [5,1,23,44,6,2,88,96,32,76,46]

i = 1
while i < len(a):
	v = a[i]
	p = i
	while 0 < p and v < a[p - 1]:
		a[p] = a[p - 1]
		p = p - 1
	a[p] = v

	i = i + 1

print a