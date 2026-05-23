class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        adj = [[] for i in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        seen = set()

        def dfs(curr):
            if curr in seen:
                return

            seen.add(curr)
            for neig in adj[curr]:
                dfs(neig)

            return

        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1

        return count

            

            