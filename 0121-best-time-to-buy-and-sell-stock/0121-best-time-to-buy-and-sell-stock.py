class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minivalue = prices[0]
        for i in range(1,len(prices)):
            profit  = prices[i]-minivalue 
            maxprofit = max(profit,maxprofit)
            minivalue = min(prices[i],minivalue)
        return maxprofit
        