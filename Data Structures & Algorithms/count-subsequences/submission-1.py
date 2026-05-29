class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        c a t.   c a a a t 

                0, 0
             1, 1.   1, 0
        2, 2   2, 1
    
        """

        n = len(s)
        m = len(t)

        memo = {}
        def dfs(i, j):
            if i == n or j == m:
                return 1 if j == m else 0

            if (i,j) in memo:
                return memo[(i, j)]
                
            if s[i] != t[j]:
                return dfs(i+1, j)

            match = dfs(i+1, j+1) + dfs(i+1, j) 
            memo[(i, j)] = match
            return match

        return dfs(0, 0)

            

            