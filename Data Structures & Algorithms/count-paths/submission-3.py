class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        def dfs(currentPath, i, j):
            if (i, j) in currentPath:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            currentPath.add((i, j))
            res = 0
            for x, y in [(0, 1), (1, 0)]:
                if 0 <= i + x < m and 0 <= j + y < n:
                    res += dfs(currentPath.copy(), i+x, j+y)
            return res
        return dfs(set(), 0, 0)
        """

        dp = [[0] * (n+1) for _ in range(m+1)]

        dp[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                dp[i][j] = dp[i][j+1] + dp[i + 1][j]

        print(dp)
        return dp[0][0]