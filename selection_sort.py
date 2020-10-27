#!usr/bin/env python

a = [5,1,23,44,6,2,88,96,32,76,46]

i = 0
while i < len(a):
	p = i
	j = i + 1
	while j < len(a):
		if a[j] < a[p]:
			p = j
		j = j + 1

	tmp = a[p]
	a[p] = a[i]
	a[i] = tmp

	i = i + 1

print a
