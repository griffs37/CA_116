#!/usr/bin/env python

s = raw_input()

i = 0 
while i < len(s) and not (s[i] >= "0" and "9" >= s[i]):
    i = i + 1
j = i
while j < len(s) and (s[j] >= "0" and "9" >= s[j]):
    j = j + 1
if j != len(s):
    print s[i:j], i
