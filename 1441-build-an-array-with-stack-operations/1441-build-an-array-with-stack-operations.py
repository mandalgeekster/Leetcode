class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stk  = []
        for i in range(1,n+1):
            if stk.count("Push")-stk.count("Pop")==len(target):
                break
            elif i in target:
                stk.append("Push")
            else:
                stk.append("Push")
                stk.append("Pop")
            
        return stk
        