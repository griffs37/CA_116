#!/usr/bin/env python

# s = "345"
s = raw_input()

# Dummy variable n
n = 0

# Index for while loop
i = 0

while i < len(s):
    # n = 3 i = 1 s[i] = "4"
    n = n + int(s[i])

    i = i + 1
    # n = 3 i = 1
print(n)
