class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 : []
        1: []
        2: []
        3: [1]

        0 -> 1 -> 2  3 -> 1
        []
        """
        adjList = {}
        for i in range(numCourses): 
            adjList[i] = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        res = []
        state = {}
        def dfs(course):
            if course in state:
                return state[course]

            state[course] = False

            for req in adjList[course]:
                if not dfs(req):
                    return False

            state[course] = True
            adjList[course] = []
            res.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


        
