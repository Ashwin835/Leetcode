class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)): #O(n) loop

            if target-numbers[i] in numbers and (target-numbers[i])>numbers[i]: #O(1)
                return [i+1, numbers.index(target-numbers[i])+1] #O(n) to search for the index
            
    #time complexity: O(n) + nO(1) + O(n)= O(n)