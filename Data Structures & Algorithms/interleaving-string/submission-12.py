class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

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

            


            


        
            
