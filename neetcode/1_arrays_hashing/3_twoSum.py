# 1. arrays & hashing

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index_dict = {}

    for index in range(len(nums)):
        complement = target - nums[index]

        if complement in index_dict:
            return [index_dict[complement], index]
        index_dict[nums[index]] = index

    return []
    
        
    
# given: only 1 valid answer exists
nums = [0, 2, 4, 6]
target = 10
print(twoSum(nums, target))

nums = [6, 4, 2, 0]
target = 10
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 0, 3]
target = 6
print(twoSum(nums, target))

"""
time: O(n)

The for loop iterates over each element in the nums array once. This loop has a time complexity of O(n), where n is the length of the nums array.
Inside the loop, each operation (comparing, accessing dictionary elements, and updating dictionary elements) is constant time, denoted as O(1).
Therefore, the overall time complexity of the code is O(n). This is because the dominant factor in determining the time complexity is the iteration over the nums array, which occurs once.

space: O(n)

The index_dict dictionary is used to store elements from the nums array. In the worst case, the dictionary could contain all the elements of the nums array. Therefore, the space required for index_dict is proportional to the size of the nums array, giving it a space complexity of O(n).
Apart from the index_dict, there are no other data structures whose space requirements depend on the size of the input.
Therefore, the overall space complexity of the code is O(n), where n is the number of elements in the nums array.
"""