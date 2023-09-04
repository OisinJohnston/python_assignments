#!/usr/bin/env python3

def get_sum(fp):
    result = 0
    lines = 0
    with open(fp) as file:
        for line in file:
           try:
               result += int(line)
               lines += 1
           except ValueError:
                print(f'Invalid integer found in file {fp} skipping...')
    return result, lines



total, linetotal = get_sum("num_calc_1.txt")
total2, linetotal2 = get_sum("num_calc_2.txt")

total += total2

linetotal += linetotal2

average = total/linetotal

print(f'average = {average}')



