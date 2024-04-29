# array, two pointers, sorting

from typing import *

def sortedSquares(nums: List[int]) -> int:
    return sorted([i**2 for i in nums])


nums = [-3, -2, -1, 0, 1, 2, 3, 4]
print(sortedSquares(nums))