class Solution(object):
    def numSquares(self, n):

        dp= [i for i in range(n+1)]
        i, i_sqr = 2, 4
        while i_sqr <= n:
            dp[i_sqr] = 1
            for j in range(i_sqr+1, len(dp)):
                dp[j] = min(dp[j], 1 + dp[j - i_sqr])
            i += 1
            i_sqr = i * i
        return dp[-1]