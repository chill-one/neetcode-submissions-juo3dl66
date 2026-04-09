class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        left = 0

        for right in range(1, len(prices)):
            while(prices[left] >  prices[right]):
                left+=1

            profit = max(prices[right]- prices[left], profit)

        return profit

            
            