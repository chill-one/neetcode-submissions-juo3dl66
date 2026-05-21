class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
          [3,  -1, 0,  1],
          [2, 2, 1, -1],
          [1,  -1, 2, -1],
          [0  ,  -1, 3,  4]
        """
        M, N = len(grid), len(grid[0])
        def dfs(i, j, count):
            if i < 0 or j < 0 or i >= M or j >= N or grid[i][j] == -1 or count > grid[i][j]:
                return

            if grid[i][j] != 0:
                grid[i][j] = min(count, grid[i][j])

            dfs(i, j+1, count + 1)
            dfs(i, j-1, count + 1)
            dfs(i+1, j, count + 1)
            dfs(i-1, j, count + 1)

            return 

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    dfs(i, j, 0)

        