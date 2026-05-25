class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = defaultdict(list)
 
        n = len(words)
        for i in range(1, n):
            prev = words[i - 1]
            curr = words[i]

            pt1 = pt2 = 0
            while pt1 < len(prev) and pt2 < len(curr) and prev[pt1] == curr[pt2]:
                pt1 += 1
                pt2 += 1

            if pt2 == len(curr) and len(prev) > len(curr):
                return ""
            if pt1 < len(prev):
                adjList[prev[pt1]].append(curr[pt2])


        print(adjList)
        

        stack = []
        dic = {}
        def dfs(curr):
            if curr in dic:
                return dic[curr]

            dic[curr] = False
            for neigh in adjList[curr]:
                if not dfs(neigh):
                    return False

            dic[curr] = True
            stack.append(curr)
            return True

        for word in words:
            for char in word:
                if not dfs(char):
                    return ""
        return "".join(stack[::-1])

            
            
            
