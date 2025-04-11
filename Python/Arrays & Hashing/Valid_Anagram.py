class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_mapping, t_mapping= dict(),dict()
        for i in range(len(s)):
            s_mapping[s[i]]= 1 + s_mapping.get(s[i],0)
            t_mapping[t[i]]= 1 + t_mapping.get(t[i],0)
        return s_mapping==t_mapping  