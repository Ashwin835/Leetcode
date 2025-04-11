class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        backwards= 1
        solution_array= [1] * len(nums)

        #runtime: O(n)
        for i in range (len(nums)-1,-1,-1):
            solution_array[i]*= backwards
            backwards*= nums[i]
        
        forwards=1 * nums[0]

        # runtime: O(n-1)
        for j in range(1,len(nums),1):
            solution_array[j]*= forwards  
            forwards*= nums[j]

        return solution_array     

#runtime: O(n)  


