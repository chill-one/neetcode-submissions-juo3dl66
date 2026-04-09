class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i : [] for i in range(numCourses)}
        set_ = set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(curr):
            if curr in set_:
                return False
            if pre_map[curr] == []:
                return True

            set_.add(curr)
            for pre_req in pre_map[curr]:
                if not dfs(pre_req):
                    return False
            set_.remove(curr)
            pre_map[curr] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
