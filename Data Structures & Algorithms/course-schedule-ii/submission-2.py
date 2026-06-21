class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {}

        for course in range(numCourses):
            adjList[course] = []

        for a, b in prerequisites:
            adjList[a].append(b)

        res = []
        visit = {}
        def dfs(curr):
            if curr in visit:
                return visit[curr]

            visit[curr] = False

            for course in adjList[curr]:
                if not dfs(course):
                    return False
            
            adjList[curr] = []
            visit[curr] = True
            res.append(curr)

            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return []
        return res

        