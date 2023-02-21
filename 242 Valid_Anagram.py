#Own implementation
#runtime: O(len(s) + len(t)) = O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict=dict()
        t_dict=dict()
        for i, j in zip(s,t):
            if i in s_dict.keys():
                s_dict[i]=s_dict.get(i)+1
            else:
                s_dict[i]=1
            if j in t_dict.keys():
                t_dict[j]=t_dict.get(j)+1
            else:
                t_dict[j]=1
        if s_dict==t_dict:
            return True
        return False
