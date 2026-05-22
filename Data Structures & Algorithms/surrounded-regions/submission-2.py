class Solution:
    def solve(self, board: List[List[str]]) -> None:
        borderZero = set()

        M, N = len(board), len(board[0])

        #Get all the zero near the border
        for i in range(M):
            if board[i][0] == "O":
                borderZero.add((i, 0))
            if board[i][N-1] == "O":
                borderZero.add((i, N-1))

        for j in range(N):
            if board[0][j] == "O":
                borderZero.add((0,j))
            if board[M-1][j] == "O":
                borderZero.add((M-1, j))

        #dfs from each border zero and mark them done as you go
        def dfs(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or board[i][j] == "#" or board[i][j] == "X":
                return

            board[i][j] = "#"
            for x, y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + x, j + y)

            return

        for i, j in borderZero:
            dfs(i, j)

        #If thier are O remaning in the board it means we could not get to it
        #Reverse # to O
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

