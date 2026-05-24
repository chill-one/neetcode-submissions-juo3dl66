class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adjList = defaultdict(list)

        for src, dst in tickets:
            adjList[src].append(dst)
            
        res = []

        def dfs(src):
            while adjList[src]:
                dfs(adjList[src].pop())
            res.append(src)

        dfs("JFK")
        return res[::-1]
