# 1. arrays & hashing

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # time: better than O(n * log(n))
    


nums = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
k = 1
print(topKFrequent(nums, k))

nums = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
k = 2
print(topKFrequent(nums, k))