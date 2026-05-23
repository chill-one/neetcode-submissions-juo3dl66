class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [a, b] where you must take course b first to take a 
        """
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        print(adjList)

        def dfs(course, seen):
            if course in seen:
                return False
            seen.add(course)
            for preReq in adjList[course]:
                if not dfs(preReq, seen):
                    return False
            seen.remove(course)
            adjList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True

