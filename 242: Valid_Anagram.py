import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s)==collections.Counter(t)
        #2n times will it add elements to the hash-table, and comparing will be 2n times
        # each operation takes O(1)
