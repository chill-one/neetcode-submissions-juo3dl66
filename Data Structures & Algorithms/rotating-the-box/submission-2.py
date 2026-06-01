class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        n = len(boxGrid[0])
        m = len(boxGrid)

        for i in range(m):
            spot = n - 1
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == "*":
                    spot = j - 1
                elif boxGrid[i][j] == "#":
                    boxGrid[i][j], boxGrid[i][spot] =  boxGrid[i][spot], boxGrid[i][j]
                    spot -=1

        print(boxGrid)
        res = [[""] * (m) for _ in range(n)]
        for i in range(n):  
            for j in range(m):
                res[i][j] = boxGrid[m - j - 1][i]


        return res
                