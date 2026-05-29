class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        word1[i] != word2[j]

        insert dfs(i, j+1)
        delete dfs(i+1, j)
        replace dfs(i+1, j+1)

        replace dfs()
        """
        n = len(word1)
        m = len(word2)
        memo = {}
        def dfs(i, j):
            operation = 0
            if j == m:
                return n - i 

            if i == n:
                return m - j 

            if (i, j) in memo:
                return memo[(i, j)]
            
            count = float("inf")
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                count = min(dfs(i+1, j), dfs(i+1, j+1), dfs(i, j+1))
            
            memo[(i, j)] =  count + 1
            return count + 1

        return dfs(0, 0)


            

            