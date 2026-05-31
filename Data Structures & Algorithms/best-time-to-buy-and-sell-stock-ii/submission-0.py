class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        on each day either buy or sell
        can sell on the same day
        i can sell any number of time as possible
        can only hold at most one share of stock at any time

        greedy approch is buy low sell high
        """

        profit = 0

        curr = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i -1]

        return profit

