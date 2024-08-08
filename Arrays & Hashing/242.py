import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s)==collections.Counter(t)
        # n= length of s and t
        #2n times will it add elements to the hash-tables, and comparing will be n times
        # each add and fetch operation takes O(1)
        #Big O: O(n)
