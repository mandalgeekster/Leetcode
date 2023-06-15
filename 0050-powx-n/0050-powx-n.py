
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def pows(x, n):
            if abs(n) == 0:
                return 1 
            elif abs(n) % 2 ==0:
                return pows(x * x, abs(n) // 2)
            else:
                return x * pows(x * x, (abs(n) - 1)//2)
        
            
        return float(pows(x, n)) if n >= 0 else 1/pows(x, n)
        