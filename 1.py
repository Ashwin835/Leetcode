class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            if target-nums[i] in visited.keys():
                return [visited[target-nums[i]],i]
            visited[nums[i]]=i

#time complexity: O(n)
