from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack =deque()
        cleanedstring=""
        
        for i in range(0,len(s)):   #O(N)
            if ord(s[i])>=97 and ord(s[i])<=122:
                stack.append(s[i])
                cleanedstring+=s[i]
                continue
            elif ord(s[i])>=65 and ord(s[i])<=90:
                y=chr(ord(s[i])+32)
                cleanedstring+=y
                stack.append(cleanedstring[-1])
            else:
                continue
        
        backwards=""

        while len(stack)!=0:  #O(1)
            cur=stack.pop()
            backwards+=cur
        

        if backwards==cleanedstring:
            return True
        return False
