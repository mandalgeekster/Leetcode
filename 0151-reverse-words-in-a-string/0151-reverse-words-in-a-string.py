class Solution:
    def reverseWords(self, s: str) -> str:
        d = s.split()
        v = d[::-1]
        ans = ""
        for i in v:
            ans = ans + " "+ str(i)
        return ans[1::]
        