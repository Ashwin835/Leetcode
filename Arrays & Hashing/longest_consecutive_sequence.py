class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_numbers= set(nums)
        longest=0

        for cur in nums:
            length=0
            if cur-1 not in unique_numbers:
                #this is a start of a new sequence
                length=1
                cur+=1
                while cur in unique_numbers:
                    length+=1
                    cur+=1
                if length>longest:
                    longest=length
        return longest