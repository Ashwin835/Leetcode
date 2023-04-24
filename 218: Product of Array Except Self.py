class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       output=[1]*len(nums)
       prefix=1
       for i in range(0,len(nums)):
           output[i]=prefix
           prefix*=nums[i]
       postfix=1
       for j in range(len(nums)-1,-1,-1):
            output[j]*=postfix
            postfix*=nums[j]
       return output


#runtime O(n+n)=O(n)

#Credits: https://leetcode.com/problems/product-of-array-except-self/solutions/3373567/prefix-and-suffix-approach/?languageTags=python3
