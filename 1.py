class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited= dict()
        for i in range (len(nums)):
            cur= nums[i]
            if (target-cur) in visited.keys(): #O(1) lookup
                return [i,visited[(target-cur)]]
            visited[cur]=i

#time complexity: O(n)
