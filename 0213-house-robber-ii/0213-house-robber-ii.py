class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for index in range(2, len(nums)-1):
            dp[index] = max((nums[index] + dp[index-2]), dp[index-1])
        
        dp1 = [0 for _ in range(len(nums))]
        lst = nums[::-1]
        dp1[0] = lst[0]
        dp1[1] = max(lst[0],lst[1])
        for index in range(2,len(nums)-1):
            dp1[index] = max((lst[index] + dp1[index-2]), dp1[index-1])
        return max(max(dp),max(dp1))
        
        