class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_of_gas = sum(gas)
        sum_of_cost = sum(cost)
        diff = 0
        start = 0
        if sum_of_gas < sum_of_cost:
            return -1 
        else:
            lst = [] 
            for i in range(len(gas)):
                diff +=  gas[i] - cost[i]
                if diff < 0:
                    start = i + 1 
                    diff = 0
            return start