class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        a a a a ->     a 

        b b b b
        """
        if len(s1) + len(s2) != len(s3):
            return False


        n, m , p = len(s1), len(s2), len(s3)

        memo = {}
        def dfs(i, j):
            k=i + j
            if i == n and j == m:
                return True if k == p else False
            
            if (i,j,k) in memo:
                return memo[(i,j,k)]

            first, second = False, False
            if i < n and s3[k] == s1[i]:
                first =  dfs(i+1, j)
            
            if j < m and s3[k] == s2[j]:
                second = dfs(i, j+1)
            
            memo[(i,j,k)] =  first or second
            return memo[(i,j,k)]

        return dfs(0,0)

            


            


        
            
