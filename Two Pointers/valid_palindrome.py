class Solution:
    def isPalindrome(self,s: str) -> bool:
        s=s.lower()
        stack= []
        output=""

        #O(n) 
        for cur in s:
            # using python ascii values, checks to see if the character is alphanumeric
            if (ord(cur)>96 and ord(cur)<123) or (ord(cur)>47 and ord(cur)<58):
                stack.append(cur)
        
        s=""
        #O(n) 
        s=s.join(stack)
        
        #O(n) 
        while len(stack)!=0:
            output+= stack.pop()
        
        if output==s:
            return True
        return False
    
    # Runtime: 3O(n) --> O(n)