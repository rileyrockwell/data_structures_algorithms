# 1. arrays & hashing

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # time: better than O(n * log(n))

    # 1. frequency dictionary
    # 2. sorted the frequency dicionary by values, using a lambda expression
    # 3. find the top k keys of the sorted frequency dictionary

    # frequency dictionary
    freq_dict = {integer: nums.count(integer) for integer in nums}

    # sort frequency dictionary by values, using a lambda expression
    # O(n * log(n)) => must find more efficient route.
    sorted_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    return [tup[0] for tup in sorted_list[:k]]

nums = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
k = 1
print(topKFrequent(nums, k))

nums = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
k = 2
print(topKFrequent(nums, k))

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

nums = [1]
k = 1
print(topKFrequent(nums, k))