class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
        """
        for i in range(len(board)):
            if(not self.isValidRow(board[i])):
                print("R")
                return False
            if(not self.isValidCol(board,i)):
                print("C")
                return False

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                if(not self.isValidBox(i, j, board)):
                    print("B")
                    return False

        return True



    def isValidRow(self, arr):
        dic = {}
        for i in range(len(arr)):
            if arr[i] == ".":
                continue
            if arr[i] in dic:
                return False
            else:
                dic[arr[i]] = True


        return True

    def isValidCol(self, arr, col):
        dic = {}
        for i in range(len(arr)):
            if arr[i][col] == ".":
                continue
            if arr[i][col] in dic:
                return False
            else:
                dic[arr[i][col]] = True

        return True

    def isValidBox(self, startRow, startCol, arr):
        dic = {}
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if arr[i][j] == ".":
                    continue
                if arr[i][j] in dic:
                    return False
                else:
                    dic[arr[i][j]] = True

        return True

            
            
                