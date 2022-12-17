class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        ans = []
        
        for s in seq:
            if s == '(':
                if not stack or stack[-1]:
                    ans.append(0)
                    stack.append(0)
                else:
                    ans.append(1)
                    stack.append(1)
            else:
                if stack[-1]:
                    ans.append(1)
                else:
                    ans.append(0)
                stack.pop()
        return ans