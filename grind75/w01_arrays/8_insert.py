from typing import *

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    def merge(intervals: List[List[int]]) -> List[List[int]]:    
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        # iterate through the rest of the intervals to merge overlapping intervals
        for start, end in intervals[1:]:
            if merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        return merged_intervals
    
    intervals.append(new_interval)

    return merge(intervals)


intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))
            
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))
