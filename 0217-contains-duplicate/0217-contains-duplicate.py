class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = True
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                flag = False
                break
            if not flag:
                break
        return not flag
