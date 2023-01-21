class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        cnt = 0
        for i in s:
            if i is "(":
                st.append(i)
            elif i is ")" and len(st)==0:
                st.append(i)
            elif i is ")" and st[-1]==")":
                st.append(i)
            else:
                st.pop()
        return len(st)
            
                
                
                
                    
                
        
        