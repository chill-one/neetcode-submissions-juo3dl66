class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))


        M, N = len(grid), len(grid[0])

        while q:
            i, j = q.popleft()
            if i + 1 < M and grid[i + 1][j] == 2147483647:
                grid[i+1][j] = grid[i][j] + 1
                q.append((i+1, j))
            
            if i - 1 >= 0 and grid[i-1][j] == 2147483647:
                grid[i-1][j] = grid[i][j] + 1
                q.append((i-1, j))

            if j + 1 < N and grid[i][j+1] == 2147483647:
                grid[i][j+1] = grid[i][j] + 1
                q.append((i, j+1))

            if j - 1 >= 0 and grid[i][j - 1] == 2147483647:
                grid[i][j-1] = grid[i][j] + 1
                q.append((i, j-1))
            print(q)
        