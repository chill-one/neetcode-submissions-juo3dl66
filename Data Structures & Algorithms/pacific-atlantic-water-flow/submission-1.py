class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        up or left ---> Pacific

        bottom or right --> Atlantic
        """
        M, N = len(heights), len(heights[0])
        canReachPacific = set()
        canReachAtlantic = set()


        def dfs(i, j, set_):
            if (i, j ) in set_:
                return
            set_.add((i, j))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + x < M and 0 <= j + y < N and heights[i][j] <= heights[i+x][j+y]:
                    dfs(i + x, j + y, set_)

            return
        #left and top for pacific
        #bottom and right for atlantic


        for i in range(N):
            dfs(0, i, canReachPacific)
            dfs(M-1,i, canReachAtlantic)


        for j in range(M):
            dfs(j, 0, canReachPacific)
            dfs(j, N-1, canReachAtlantic)
        

        res = []
        for i, j in (canReachPacific & canReachAtlantic):
            res.append([i,j])

        return res



        


