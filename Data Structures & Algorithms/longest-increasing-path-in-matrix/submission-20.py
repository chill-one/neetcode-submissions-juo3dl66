class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #dp = [[1] * (len(matrix[0]) for _ in range(len(matrix))]

        sys.setrecursionlimit(20000)
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]
            count = 1

            for x , y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                if 0 <= i + x < m and 0 <= j + y < n and matrix[i + x][j + y] > matrix[i][j]:
                    count = max(1 + dfs(i + x, j + y), count) 
            
            memo[(i, j)] = count
            return count

        maxCount = 0
        for i in range(m):
            for j in range(n):
                    maxCount = max(dfs(i, j), maxCount)
        
        return maxCount