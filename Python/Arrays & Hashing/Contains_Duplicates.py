class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        for cur in nums:
            if cur in visited:
                return True
            visited.add(cur)
        return False