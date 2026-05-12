class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        arr = [float("inf")]
        def dfs(idx, c):
            if idx >= len(cost):
                arr[0] = min(arr[0], c)
                return

            dfs(idx+1, c + cost[idx])
            dfs(idx+2, c + cost[idx])

        dfs(0, 0)
        dfs(1, 0)
        """
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i - 2] + cost[i-2])


        return dp[-1]

            