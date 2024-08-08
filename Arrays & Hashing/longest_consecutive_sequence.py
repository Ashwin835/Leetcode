class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length=0
        nums= set(nums)
        
        for cur in nums:
            cur_length=0
            if cur-1 not in nums:
                cur_length+=1
                while (cur_length + cur) in nums:
                    cur_length+=1
            if cur_length> longest_length:
                longest_length= cur_length
        return longest_length  