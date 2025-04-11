class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        visited= {}
        return_list=[]
        #let n = number of elements in nums

        #O(n) operation
        for cur in nums:
            visited[cur]=1 + visited.get(cur,0)
        
        #Bucket sort
        sortings= [[] for i in range(len(nums)+1)]

        #O(n) operation
        for key, value in visited.items():
            sortings[value].append(key)
        
        #O(n) operation
        for i in range (len(nums), 0, -1):
            for current in sortings[i]:
                return_list.append(current)
                if len(return_list)==k:
                    return return_list
        
        #time complexity: 3O(n)= O(n)
