class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution= [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                continue
            product= nums[i+1]*solution[i+1]
            solution[i]*=product
        

        value=1
        for j in range(len(nums)):
            if j==0:
                continue
            product= nums[j-1] * value
            value=product
            solution[j]*=product
        return solution 
#Big O: O(2n) = O(n) 
