#!/usr/bin/env python3
with open('numbers', 'w') as numbers:
    for i in range(10):
        numbers.write(input(f"{i+1}. Give me a number: ")+'\n')




