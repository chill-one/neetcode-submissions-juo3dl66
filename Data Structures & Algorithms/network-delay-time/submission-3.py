class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}

        for i in range(1, n+1):
            adjList[i] = []

        for src, dst, time in times:
            adjList[src].append((dst, time))

        visited = [False] * (n)
        h = [(0, k)]

        currTime = 0
        while h:
            time, curr = heapq.heappop(h)

            if visited[curr-1]:
                continue
            currTime = time
            for dst, time in adjList[curr]:
                heapq.heappush(h, (time + currTime, dst))

            visited[curr-1] = True


        for visit in visited:
            if not visit:
                return -1

        return currTime