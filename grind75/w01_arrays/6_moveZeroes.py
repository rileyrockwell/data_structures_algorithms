# array, two pointers

from typing import *

def moveZeros(nums: List[int]) -> None:
    
    # if returning
    
    # return_list = []

    # for i in reversed(nums):
    #     if i == 0:
    #         return_list.append(i)
    #     else:
    #         return_list.insert(0, i)

    # return return_list

    # if not returning. modify numers in-place.

    for i in reversed(nums):
        if i == 0:
            nums.insert(len(nums) - 1, i)
        else:
            nums.insert(0, i)

    return nums



nums = [0, 1, 0, 2, 3, 0]
print(moveZeros(nums))

nums = [0, 1, 0, 3, 12]
print(moveZeros(nums))