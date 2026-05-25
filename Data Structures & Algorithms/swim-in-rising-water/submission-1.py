class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [(0, 0,0)]
        seen = set()

        bottleNeck = float("inf")


        while h:
            t, x, y = heapq.heappop(h)
            if (x, y) in seen:
                continue
            seen.add((x,y))

            current_max = max(t, grid[x][y])
            if x == n -1 and y == n - 1:
                bottleNeck = min(bottleNeck, current_max)

            
            for i, j in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + i < n and 0 <= y + j < n:
                    heapq.heappush(h, (current_max, x + i, y + j))


        return bottleNeck

        