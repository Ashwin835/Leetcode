class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited= set()
        for cur in nums:
            if cur in visited: #O(1) hashing lookup time
                return True
            else:
                visited.add(cur)  
        return False 
