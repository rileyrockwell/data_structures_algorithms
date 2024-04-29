# 1. arrays & hashing

from typing import List

def groupAnagrams(strings: List[str]) -> List[List[str]]:
    # arrays & hashing
    anagrams = {}

    for string in strings:
        key = "".join(sorted(string))
        
        # print(key, string)

        if key not in anagrams:
            anagrams[key] = []
            anagrams[key].append(string)
        else:
            anagrams[key].append(string)

    return list(anagrams.values())


strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strings))

strings = [""]
print(groupAnagrams(strings))

strings = ["a"]
print(groupAnagrams(strings))

"""
time: ...

space: ...
"""