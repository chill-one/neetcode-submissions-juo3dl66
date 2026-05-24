class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        h = [(0,0)]
        visited = [False] * n
        cost = [float("inf") for _ in range(n)]
        cost[0] = 0
        while h:

            c, v = heapq.heappop(h)

            if visited[v]:
                continue

            visited[v] = True
            for idx, coord in enumerate(points):
                if visited[idx]:
                    continue
                x1, y1 = coord
                x2, y2 = points[v]

                toCost = abs(x2 - x1) + abs(y2 - y1)

                if toCost != 0:
                    cost[idx] = min(cost[idx], toCost)
                    heapq.heappush(h, (toCost, idx))
        print(cost)
        return sum(cost) 



            
            
