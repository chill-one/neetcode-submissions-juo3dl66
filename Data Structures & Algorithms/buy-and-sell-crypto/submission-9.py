class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_prof = 0

        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right

            max_prof = max(max_prof, prices[right] - prices[left])

        return max_prof