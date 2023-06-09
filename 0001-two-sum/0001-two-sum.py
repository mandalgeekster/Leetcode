class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = {}
        for i, j in enumerate(nums):
            if target - j in k:
                return k[target-j], i
            k[j]=i
                
        