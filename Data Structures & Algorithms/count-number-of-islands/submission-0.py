class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        been = [
            [False for i in range(len(grid[0]))] for i in range(len(grid))
                ]

        Row, Col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= Row or c >= Col or grid[r][c] == "0" or been[r][c]:
                return 

            been[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for r in range(Row):
            for c in range(Col):
                if not been[r][c] and grid[r][c] == "1":
                    dfs(r, c)
                    res+=1

        return res



