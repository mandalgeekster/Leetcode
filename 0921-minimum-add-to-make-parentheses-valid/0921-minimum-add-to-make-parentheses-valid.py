class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for i in range(len(s)):
            if s[i]=='(':
                stk.append(s[i])
            elif s[i]==')':
                if stk and stk[-1] =='(':
                    stk.pop()
                else:
                    stk.append(s[i])
        return len(stk)
                
	
	    
