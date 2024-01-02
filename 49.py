class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [[strs[0]]]

        results=dict()
        for cur in strs:
            alphabet= [0]* 26
            for letter in cur: 
                alphabet[ord(letter)-ord('a')]+=1
            string_rep= str(alphabet)
            if string_rep in results.keys():
                array= results[string_rep]
                array.append(cur)
                results[string_rep]= array
            else:
                results[string_rep]= [cur]
        return list(results.values())
      #O(n^2)
