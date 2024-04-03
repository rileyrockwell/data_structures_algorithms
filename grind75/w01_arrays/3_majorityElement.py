# array, hashtable, divide and conquer, sorting, counting

from typing import *

def majorityElement(nums: List[int]) -> int:
    
    # count the number of occureneces of an integer in "nums"
    freq_dict = {integer: nums.count(integer) for integer in nums}

    # generate the same dictionary as before, with keys and values swaped
    swaped_freq_dict = {nums.count(integer): integer for integer in nums}
    
    # determine the maximum value of all frequencies
    max_freq = max(freq_dict.values())

    # call the original integer associated with the maxium value of all frequencies
    return swaped_freq_dict[max_freq]


# given: there will always exist a majority element
nums = [0, 1, 2, 1, 1]
nums = [3, 2, 3]
print(majorityElement(nums))