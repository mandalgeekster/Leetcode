class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        cn = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for i in s:
            if i in cn:
                st += i
        low = st.lower()
        return low == low[::-1]
            
        