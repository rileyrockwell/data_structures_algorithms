# 1. arrays & hashing

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # arrays & hashing...in less than O(n^2) time
    
    # use a hashmap (dictionary)

    # 1. map each element to its respective index
    # 2. find the complement and determine if the complement equals target

    # map each element of nums to its respective index
    index_dict = {integer: index for index, integer in enumerate(nums)}

    for index in range(len(nums)):
        complement = target - nums[index]

        if complement in nums:
            return [index, index_dict[complement]]

    
        
    
# given: only 1 valid answer exists
nums = [0, 2, 4, 6]
target = 10
print(twoSum(nums, target))

nums = [6, 4, 2, 0]
target = 10
print(twoSum(nums, target))