class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Row, Col = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, set_, prevHeight):
            if (r < 0 or c < 0 or r == Row or 
            c == Col or heights[r][c] < prevHeight or
            (r, c) in set_):
                return 

            set_.add((r,c))
            dfs(r + 1, c, set_, heights[r][c])
            dfs(r - 1, c, set_, heights[r][c])
            dfs(r , c + 1, set_, heights[r][c])
            dfs(r , c - 1, set_, heights[r][c])


        for c in range(Col):
            dfs(0, c, pac, heights[0][c])
            dfs(Row - 1, c, atl, heights[Row - 1][c])

        for r in range(Row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Col - 1, atl, heights[r][Col - 1])

        res = []
        for r in range(Row):
            for c in range(Col):
                if (r,c) in pac and (r, c) in atl:
                    res.append([r,c])

        return res
