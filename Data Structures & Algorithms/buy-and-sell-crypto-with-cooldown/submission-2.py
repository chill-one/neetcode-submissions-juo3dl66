class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        memo = {}
        n = len(prices)
        def dfs(i, buying):
            if i >= n:
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]            
            res = 0

            if buying:
                res = max(dfs(i + 1, False) - prices[i], dfs(i+1, True), res)
            else:
                res =  max(prices[i] + dfs(i + 2, True), dfs(i+1, False), res)
            
            memo[(i, buying)] = res
            return res
        return dfs(0,True)
        """
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * (n + 1) for i in range(3)]
        dp[0][0] = -float('inf')

        for i in range(1, n + 1):
            dp[0][i] = max(dp[0][i-1], dp[2][i-1] - prices[i-1])
            dp[1][i] = dp[0][i-1] + prices[i-1]
            dp[2][i] = max(dp[2][i-1], dp[1][i-1])

        return max(dp[1][n], dp[2][n])