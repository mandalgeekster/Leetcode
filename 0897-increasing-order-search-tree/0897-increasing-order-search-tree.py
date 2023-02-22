# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        final = self.data = TreeNode 
        def inorder(node):
            if node:
                inorder(node.left)
                self.data.right = TreeNode(node.val)
                self.data = self.data.right 
                inorder(node.right)
        inorder(root)
        return final.right
                
        