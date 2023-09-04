#!/usr/bin/env python3


nums = [int(input(f'{i+1}. Please give a number : ')) for i in range(20)]
avg = sum(nums)/len(nums)
print(f'the average is {avg}')




