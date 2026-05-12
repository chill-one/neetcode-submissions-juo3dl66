class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        3x3
        """
        found = []

        def dfs(i, path, colMap, negdiag, posdiag):
            if i >= n:
                found.append(path)
                return

            for col in range(n):
                if col not in colMap and i + col not in posdiag and i - col not in negdiag:
                    posdiag.add(i + col)
                    negdiag.add(i - col)
                    colMap.add(col)
                    path.append(col)
                    dfs(i + 1,path[:], colMap, negdiag, posdiag)
                    path.pop()
                    colMap.remove(col)
                    posdiag.remove(i + col)
                    negdiag.remove(i - col)

        def convert(arr):
            board = []
            x = 0
            for y in arr:
                curr = ["."] * n
                curr[y] = "Q"
                board.append("".join(curr))

            return board
        
        dfs(0 ,[],set(), set(), set())

        res = []
        for arr in found:
            res.append(convert(arr))
        return res