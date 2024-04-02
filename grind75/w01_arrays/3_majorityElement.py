from typing import *

def majorityElement(nums: List[int]) -> int:
    
    freq_dict = {integer: nums.count(integer) for integer in nums}

    max_val = max(freq_dict.values())

    return max_val



# given: there will always exist a majority element
nums = [0, 1, 2, 1, 1]

print(majorityElement(nums))