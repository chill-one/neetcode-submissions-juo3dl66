class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        dp[-1][-1] = True

        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[i]) - 1, -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True

                if  j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


    
        """
        n, m , p = len(s1), len(s2), len(s3)

        memo = {}
        def dfs(i, j):
            k=i + j
            if i == n and j == m:
                return True 
            
            if (i,j) in memo:
                return memo[(i,j)]
                
            if i < n and s3[k] == s1[i] and dfs(i+1, j):
                return True
            
            if j < m and s3[k] == s2[j] and dfs(i, j+1):
                return True
            
            memo[(i,j)] =  False
            return False

        return dfs(0,0)
        """

            


            


        
            
