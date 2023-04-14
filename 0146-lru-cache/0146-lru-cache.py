class LRUCache:

    def __init__(self, capacity: int):       
        self.memory={}
        self.stack=[]
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key in self.memory:
            self.updateStack(key)
            return self.memory[key]
        return -1 
    
    def updateStack(self, key:int) -> None:
        if key in self.stack:
            curIndex = self.stack.index(key)
            self.stack.pop(curIndex)
        self.stack.append(key)

    def put(self, key: int, value: int) -> None:
        if len(self.memory) == self.capacity and (key not in self.memory):
            lastKey = self.stack.pop(0)
            self.memory.pop(lastKey)
        self.memory[key] = value
        self.updateStack(key)
        





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)