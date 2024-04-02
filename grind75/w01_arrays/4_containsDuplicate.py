# array, hashtable, sorting

from typing import *

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))

nums = [0, 1, 0]
print(containsDuplicate(nums))
