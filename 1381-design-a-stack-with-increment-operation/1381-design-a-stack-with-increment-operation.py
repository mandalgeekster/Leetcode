class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            (self.stack).append(x)
        
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

        

    def increment(self, k: int, val: int) -> None:
        s = min(k,len(self.stack))
        if k<=len(self.stack):
            for i in range(k):
                self.stack[i]+=val
        else:
            for i in range(len(self.stack)):
                self.stack[i]+=val
                
        #for i in range(s):
      #      self.stack[i] += val
           # for j in range(len(self.stack)):
            #    self.stack[j]+=val
            #[x+val for x in self.stack]
        #else:
         #   for i in range(k+1):
         #       self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)