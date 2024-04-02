from typing import *

def majorityElement(nums: List[int]) -> int:
    
    freq_dict = {integer: nums.count(integer) for integer in nums}

    # return freq_dict

    index_dict = {integer: index for index in enumerate(nums)}

    return index_dict


# given: there will always exist a majoirty element
nums = [0, 1, 2, 1, 1]

print(majorityElement(nums))