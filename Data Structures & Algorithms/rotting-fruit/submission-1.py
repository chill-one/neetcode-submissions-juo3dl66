class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])

        q = deque()
        freshCount = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        if freshCount == 0:
            return 0

        minute = 0

        while q:
            currentLevel = len(q)
            olfFreshCount = freshCount
            for _ in range(currentLevel):
                i, j = q.popleft()

                if i + 1 < M and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    freshCount -= 1
                    q.append((i+1, j))

                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    freshCount -= 1
                    q.append((i-1, j))


                if j + 1 < N and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    freshCount -= 1
                    q.append((i, j+1))
 

                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    freshCount -= 1
                    q.append((i, j-1))

            if olfFreshCount != freshCount:
                minute += 1

        return minute if freshCount == 0 else -1
 
