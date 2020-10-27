#!/usr/bin/env python

import sys

german = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

a = sys.stdin.read().split()

i = 0
while i < len(a):
    if a[i] in german:
        print german[a[i]]
    i = i + 1
