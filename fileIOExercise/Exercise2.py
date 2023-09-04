#!/usr/bin/env python3

lines = 0

with open('daffodils.txt') as file:
    for line in file:
        lines += 1

print(f"there are {lines} lines in the file daffodils.txt")
