#!/usr/bin/env python

import sys
 n = int(sys.argv[1])
s = raw_input()

total = 0
i = 0
while i < len(s) and total != n:
     if s[i] == ",":
         total = total + 1
     i = i + 1
 
 j = i
 while i < len(s) and s[i] != ",":
     i = i + 1
      print s[j:i]
