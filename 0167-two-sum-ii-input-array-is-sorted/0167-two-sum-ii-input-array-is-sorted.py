class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left < right:
            cursum = nums[left] + nums[right]
            
            if cursum > target:
                right -= 1 
            elif cursum < target:
                left += 1
            else:
                return[left+1 ,right+1]
           