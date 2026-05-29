class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(len(dp[0])):
            dp[-1][i] = 1

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if j < n and i < m:
                    if  s[j] != t[i]:
                        dp[i][j] += dp[i][j + 1]
                    else:
                        dp[i][j] += dp[i][j+1] + dp[i+1][j+1]

        return dp[0][0]



            

            