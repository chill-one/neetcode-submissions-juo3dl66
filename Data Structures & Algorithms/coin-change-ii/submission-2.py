class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        memo = {}
        def dfs(i,total):
            if i >= len(coins) or total > amount:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            if total == amount:
                return 1

            res = dfs(i, total + coins[i]) + dfs(i+1, total)
            
            memo[(i, total)] = res
            return res
        return dfs(0, 0)
        """
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][amount] = 1

        for i in range(n - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                include = dp[i][j + coins[i]] if j + coins[i] <= amount else 0
                exclude = dp[i+1][j]
                dp[i][j] = include + exclude

        return dp[0][0]
