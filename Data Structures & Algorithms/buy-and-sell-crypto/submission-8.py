class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_price = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right

            max_price = max(max_price, prices[right] - prices[left])

        return max_price


            
            