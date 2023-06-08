from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_of_list = prod(nums)
        ans = [] 
        for i in nums:
            if i != 0:          
                ans_of_one = prod_of_list//i 
                ans.append(ans_of_one)
            else:
                temp = nums.copy() 
                remove_zero = temp.remove(0)
                prod_zero = prod(temp)
                ans.append(prod_zero)
        return ans
        
        