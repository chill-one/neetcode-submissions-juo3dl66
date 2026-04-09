class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        row = [False] * M
        col = [False] * N
        

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                   row[i] = True
                   col[j] = True


        for i in range(M):
            if row[i]:
                for j in range(N):
                    matrix[i][j] = 0
            
        for i in range(N):
            if col[i]:
                for j in range(M):
                    matrix[j][i] = 0

        
        