#from sys import maxint
class Solution:
    #from sys import maxint
    def maxSubArray(self, nums: List[int]) -> int:
        maxi_s = -10**9-1
        maxi = 0
        for i in range(len(nums)):
            maxi = maxi + nums[i]
            if maxi_s < maxi:
                maxi_s = maxi 
            if maxi < 0 :
                maxi  = 0 
        return maxi_s
        