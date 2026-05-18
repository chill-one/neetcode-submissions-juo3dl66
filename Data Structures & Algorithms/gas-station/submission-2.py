class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1


        total = 0
        result = 0
        for idx in range(len(gas)):
            if total < 0:
                total = 0
                result = idx 

            total += gas[idx] - cost[idx]

        return result

