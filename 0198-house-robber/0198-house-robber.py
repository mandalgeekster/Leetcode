class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(i,nums,dp):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if dp[i]!=-1:
                return dp[i]
            pick = nums[i]+f(i-2,nums,dp)
            non_pick = f(i-1,nums,dp)
            dp[i] = max(pick,non_pick)
            return dp[i]
        dp= [-1]*(len(nums)+1)
        return f(len(nums)-1,nums,dp)
  
        