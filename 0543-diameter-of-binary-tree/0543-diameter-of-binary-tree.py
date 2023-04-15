# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ttl = 0
        def depth(root):
            if root is None: 
                return 0
            #print(root)
            left = depth(root.left) 
            right = depth(root.right) 
            #print(left,right)
            self.ttl = max(self.ttl, left+right)
            return 1 + max(left, right)
        depth(root)
        return self.ttl
        