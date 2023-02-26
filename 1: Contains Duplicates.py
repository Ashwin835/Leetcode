class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     solution=[]
     for i in range(0,len(nums)): #O(n) for loop
         other_index=target-nums[i]
         if other_index in solution: #get method O(1)
            j=solution.index(other_index) #O(1)
            return [i,j] 
         solution.append(nums[i]) #adding to end is O(1) except for allocate


##BIG O: O(len(nums))=O(n)
