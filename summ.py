#!/usr/bin/env python

i = 0
while i < len(a) - 1:   # <-- So we can stop one iteration earlier.
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