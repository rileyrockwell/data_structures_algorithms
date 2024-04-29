# 1. arrays & hashing

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s = "testing"
t = "gnitest"
print(isAnagram(s, t))

s = "hannah"
t = "hahann"
print(isAnagram(s, t))

s = "water"
t = "watered"
print(isAnagram(s, t))

"""
time: ...

space: ...
"""