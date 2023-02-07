# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root,stk):
            if not root:
                return None
            inorder(root.left,stk)
            stk.append(root.val)
            inorder(root.right,stk)
        stk = [] 
        maxi = 10**5+1
        ans = 0
        inorder(root,stk)
        for i in range(1,len(stk)):
            maxi = min(abs(stk[i]-stk[i-1]),maxi)
        return maxi
        