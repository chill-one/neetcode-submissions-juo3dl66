class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        A stone '#'
        A stationary obstacle '*'
        Empty '.'
        """
        m, n = len(boxGrid), len(boxGrid[0])

        for i in range(m):
            emptyCell = n - 1
            for r in range(n - 1, -1, -1):
                """
                if boxGrid[i][r] == ".":
                    emptyCell = r
                """
                if boxGrid[i][r] == "#":
                    """
                    while emptyCell >= r and boxGrid[i][emptyCell] != ".":
                        emptyCell -= 1
                    """
                    boxGrid[i][emptyCell], boxGrid[i][r] = boxGrid[i][r], boxGrid[i][emptyCell]
                    emptyCell -= 1
                elif boxGrid[i][r] == "*":
                    emptyCell = r - 1

            
        res = [[""] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = boxGrid[i][j]


        return res
            

            
