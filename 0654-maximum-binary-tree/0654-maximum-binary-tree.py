# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums :
            return None
        maxi = max(nums)
        ind = nums.index(maxi)
        node  = TreeNode(maxi)
        node.left = self.constructMaximumBinaryTree(nums[0:ind])
        node.right = self.constructMaximumBinaryTree(nums[ind+1:])
        return node
        