class Solution:
    def getSum(self, a: int, b: int) -> int:
            maxi = max(a, b)
            mini = min(a, b)
            if a == 0 or b == 0:
                return a or b 
            else:

                quo = maxi//mini 
                rem = maxi%mini 
                ans = quo*mini + mini + rem
                return ans
           
        