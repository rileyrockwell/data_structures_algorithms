# 1. arrays & hashing

from typing import List

def containsDuplicate(arr: List[int]) -> bool:
    return len(set(arr)) != len(arr)

arr = [1, 2]
print(containsDuplicate(arr))

arr = [1, 1, 2]
print(containsDuplicate(arr))

arr = []
print(containsDuplicate(arr))

"""
time: ...

space: ...
"""