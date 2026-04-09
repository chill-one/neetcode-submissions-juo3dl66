class Solution:
    def validRow(self, row, board):
        dic = {}
        for i in range(len(board)):
            if board[row][i] == '.':
                continue
            if board[row][i] in dic:
                return False
            dic[board[row][i]] = True
        return True

    def validCol(self, col, board):
        dic = {}
        for i in range(len(board)):
            if board[i][col] == '.':
                continue
            if board[i][col] in dic:
                return False
            dic[board[i][col]] = True
        return True

    def validBox(self, s_row, s_col, e_row, e_col,board):
        dic = {}

        for i in range(s_row, e_row):
            for j in range(s_col, e_col):
                if board[i][j] == '.':
                    continue
                if board[i][j] in dic:
                    return False
                dic[board[i][j]] = True
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        for i in range(N):
            if not self.validRow(i, board):
                return False
            if not self.validCol(i, board):
                return False

        for i in range(0, N):
            row, col = (i // 3) * 3, (i % 3) *3
            if not self.validBox(row, col, row+3, col+3, board):
                return False

        return True

        


