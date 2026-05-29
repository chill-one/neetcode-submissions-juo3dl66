class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        
        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                if word1[j- 1] == word2[i- 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

        return dp[-1][-1]

                




            

            