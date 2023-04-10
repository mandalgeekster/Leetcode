# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stk = [(root, 0)]
        wdth = 0 
        while stk:
            n = len(stk)
            left = stk[0][1]
            right = stk[-1][1] 
            wdth = max(wdth, right-left+1)
            for i in range(n):
                node, ps = stk.pop(0)
                if node.left:
                    stk.append((node.left, ps*2))
                if node.right:
                    stk.append((node.right, ps*2+1))
            for i in range(len(stk)):
                stk[i] = (stk[i][0], stk[i][1]-left)
        return wdth
                
        