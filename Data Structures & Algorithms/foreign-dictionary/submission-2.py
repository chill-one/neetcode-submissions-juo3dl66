class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for idx in range(len( words) - 1):
            a, b = words[idx], words[idx + 1]
            minLen = min(len(a), len(b))
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""

            for j in range(minLen):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break

        visit = {}
        res = []

        print(adj)

        def dfs(char):
            if char in visit:
                return visit[char]

            visit[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visit[char] = False
            res.append(char)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
            
