class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for i in range(n)] for i in range(m)]
        cache[-1][-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if i == (m - 1) and j == (n - 1):
                    continue
                if i + 1 < m:
                    cache[i][j] += cache[i + 1][j]
                if j + 1 < n:
                    cache[i][j] += cache[i][j + 1]
        return cache[0][0]
        