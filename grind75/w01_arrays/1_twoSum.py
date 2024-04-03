# topics: array, hashtable

from typing import *

def twoSum(arr: List[int], target: int) -> List[int]:

	index_dict = {}
	
	# assign index values to the respective integers in "arr"
	for index, number in enumerate(arr):
		
		# determine the complement (to be used in following conditional)
		complement = target - number

		# if the complement exists, then the indexed valued associated with
		# the iteration, becomes the answer
		if complement in index_dict:
			
			# return the complement and index (obtained from the same iterative cycle)
			return [index_dict[complement], index]

		# if the complement does not exist, assign it to the dictionary.
		index_dict[number] = index
		

arr = [0, 1, 0, 2]
target = 3
print(twoSum(arr, target))