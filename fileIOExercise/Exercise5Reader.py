#!/usr/bin/env python3
total = 0
amount = 0
with open('numbers') as numbers:
    for line in numbers:
        try:
            total += int(line)
            amount += 1
        except ValueError:
            print('invalid number in file skipping...')

print(f"Average = {total/amount}")
