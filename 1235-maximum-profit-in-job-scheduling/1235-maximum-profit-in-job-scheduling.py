class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        arr = []
        
        for i in range(len(profit)):
            arr.append((startTime[i], endTime[i], profit[i]))
            
        arr.sort(key=lambda x : x[0])
        helperDict = dict()

        return self.calculateProfit(arr, 0, helperDict)
    
    
    def calculateProfit(self, arr, idx, helperDict):
        if idx >= len(arr):
            return 0
        
        if idx in helperDict:
            return helperDict[idx]
        
        _, end, curr_profit = arr[idx]
        
        for i in range(idx+1, len(arr)):
            if arr[i][0] >= end:
                curr_profit += self.calculateProfit(arr, i, helperDict)
                break
                
        profit_without_curr_idx = self.calculateProfit(arr, idx+1, helperDict)
        
        max_profit = max(curr_profit, profit_without_curr_idx)
        
        helperDict[idx] = max_profit
        
        return max_profit
