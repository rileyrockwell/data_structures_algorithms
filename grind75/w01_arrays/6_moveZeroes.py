# array, two pointers

from typing import *

# submitted to leetcode
def moveZeroes(nums: List[int]) -> None:
    # think about the problem in a new way.
    # stop w/ old ways of thinking.


# algomonster solution
def moveZeroes(nums: List[int]) -> None:
    last_non_zero_index = 0

    for current, value in enumerate(nums):
        # when a non-zero element is found
        if value != 0:
            # swap
            nums[last_non_zero_index], nums[current] = nums[current], nums[last_non_zero_index]
            
            # increment
            last_non_zero_index += 1

    # return nothing: "modify nums in-place."


nums = [0, 1, 0, 2, 3, 0]
print(moveZeroes(nums))

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))