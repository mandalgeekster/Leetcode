class MinStack:

    def __init__(self):
        self._data = []
        self.stack = []
        
        

    def push(self, val: int) -> None:
        self._data.append(val)
        val = min(val, self.stack[-1] if self.stack else val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self._data.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self._data[-1]
        
    
        
        

    def getMin(self) -> int:
        return self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()