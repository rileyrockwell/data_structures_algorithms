from typing import *

# alogmonster solution
def insert(inteverals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # explain...    
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        #         
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        # iterate through the rest of teh intervals to merge overlapping ones.
        for start, end in intervals[1:]:
            # explain...
            