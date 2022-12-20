#!/usr/bin/env python3

import sys
from collections import deque

def mix(nums):
    len_nums = len(nums)

    for i in range(len_nums):
        while True:
            if nums[0][0] == i:
                break
            nums.append(nums.popleft())
            
        cur = nums.popleft()
        rotate_by = cur[1]  % (len_nums - 1)
        for i in range(rotate_by):
            nums.append(nums.popleft())
        nums.append(cur)
        
    return nums

def score_nums(nums):
    len_nums = len(nums)
    while nums[0][1] != 0:
        nums.append(nums.popleft())
        
    return sum(nums[c % len_nums][1] for c in [1000, 2000, 3000])

with open(".\day_20\input.txt", 'r') as f:
    numbers = list(map(int, f.readlines()))
    
nums = deque(enumerate(numbers))

nums = mix(nums)
part1 = score_nums(nums)
print(f'Part 1: {part1}')

nums2 = deque((i,n * 811589153) for i,n in enumerate(numbers))
for _ in range(10):
    nums2 = mix(nums2)
part2 = score_nums(nums2)
print(f'Part 2: {part2}')