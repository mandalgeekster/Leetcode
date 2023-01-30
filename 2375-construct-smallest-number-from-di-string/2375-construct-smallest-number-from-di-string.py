class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk = []
        ans = ""
        num = 1 
        n = len(pattern)
        for i in range((n)):
            if pattern[i]=='D':
                stk.append(num)
                num+=1 
            else:
                stk.append(num)
                num+=1 
                while stk:
                    last = stk.pop()
                    ans+=str(last)
        stk.append(num)
        while stk:
            last  = stk.pop()
            ans+=str(last)
        return ans
                    
        