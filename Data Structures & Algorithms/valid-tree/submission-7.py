class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjList = {}
        for i in range(n):
            adjList[i] = []

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)


        seen = set()
        def dfs(curr, prev):
            if curr in seen:
                return False

            seen.add(curr)
            for edge in adjList[curr]:
                if edge != prev and not dfs(edge, curr):
                    return False

            return True

        
        return dfs(0, -1) and len(seen) == n and len(edges) == n - 1



        

        


        


        