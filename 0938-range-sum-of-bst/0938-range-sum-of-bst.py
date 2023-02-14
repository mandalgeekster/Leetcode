# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stk = [root]
        ans = 0 
      #  print(stk)
        while stk:
            node = stk.pop()
          #  print(node)
            if low<=node.val<=high:
                ans+=node.val
            if node.left:
                stk.append(node.left)
               # print(stk)
            if node.right:
                stk.append(node.right)
               # print(stk)
        return ans
    
    #[TreeNode{val: 10, left: TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None},
# right: TreeNode{val: 7, left: None, right: None}},
 # right: TreeNode{val: 15, left: None,
 #  right: TreeNode{val: 18, left: None, right: None}}}]