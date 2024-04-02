# topics: ...

from typing import *

def twoSum(arr: List[int], target: int) -> List[int]:

	index_dict = {}
	
	for index, number in enumerate(arr):
		
		complement = target - number

		if complement in index_dict:
			
			return [index_dict[complement], index]

		index_dict[number] = index
		

arr = [0, 1, 0, 2]
target = 3
print(twoSum(arr, target))