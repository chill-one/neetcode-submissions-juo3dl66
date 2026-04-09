class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_prof = 0

        for right, price in enumerate(prices):
            if prices[left] > price:
                left = right


            max_prof = max(max_prof, price - prices[left])


        return max_prof