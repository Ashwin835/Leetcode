class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
            counts= dict()
            for cur in nums: #O(n)
                if cur not in counts.keys(): #O(1) lookup
                    counts[cur]=1 #adding this is O(1) 
                else:
                    counts[cur]= counts.get(cur)+1 #updating is O(1)
            sorted_counts= dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)) #O(nlogn to sort)
            return list(sorted_counts.keys())[:k]
#runtime: O(n) + O(nlogn)= O(n)
#source for sorted() method: https://flexiple.com/python/python-sort-dictionary-by-value
