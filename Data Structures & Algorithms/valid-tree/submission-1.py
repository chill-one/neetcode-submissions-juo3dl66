class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for to in adj[curr]:
                if to == prev:
                    continue
                if not dfs(to, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
