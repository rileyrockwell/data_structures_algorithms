from typing import *

### 1 ### https://leetcode.com/problems/two-sum/description/
def twoSum(nums: List[int], target: int) -> List[int]:
        # O(n) solution
        seen = {}  # Dictionary to store the indices of numbers we've seen so far
        for i, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                        return [seen[complement], i]  # Found the indices of the two numbers
                seen[num] = i  # Store the current number's index
        return []  # If no solution is found


### 2 ### https://leetcode.com/problems/majority-element/description/
def majorityElement(nums: List[int]) -> int:
        n = len(nums)
        freq_dict = {element: nums.count(element) for element in nums}
        m_e_occurences = n / 2

        for key in freq_dict.keys():
                if freq_dict[key] > m_e_occurences:
                        return key


### 3 ### https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


### 4 ### https://leetcode.com/problems/move-zeroes/description/
def moveZeroes(nums: List[int]) -> None:
        """
        move all zeros w/in the nums array to the end of the array, while
        maintaining the relative (original) order of the non-zero elements.
        
        do not return anything; modify nums in-place.
        """
        for element in nums:
                if element == 0:
                        nums.remove(element)
                        nums.append(0)

        return nums
        

### 5 ### https://leetcode.com/problems/insert-interval/
def insert(intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
        pass



if __name__ == "__main__":
        # two sum
        nums = [0, 1, 2, 2]
        target = 4
        print(twoSum(nums, target))

        # majority element
        nums = [0, 1, 0, 1, 0]
        nums = [1, 1, 2, 2, 2, 1, 1]
        print(majorityElement(nums))

        # contains duplicate
        nums = [0, 0]
        nums = [0, 1]
        nums = [0, 1, 0]
        print(containsDuplicate(nums))

        # move zeroes
        nums = [0, 0, 3, 2, 1]
        print(moveZeroes(nums))
        nums = [0, 1]
        print(moveZeroes(nums))
