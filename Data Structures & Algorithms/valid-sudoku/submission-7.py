class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid_col(col):
            nums = [False] * 9

            for row in range(len(board)):
                if board[row][col].isdigit():
                    idx = ord(board[row][col]) - ord("1")
                    if nums[idx]:
                        return False
                    nums[idx] = True
            return True

        def valid_row(row):
            nums = [False] * 9

            for col in range(len(board)):
                if board[row][col].isdigit():
                    idx = ord(board[row][col]) - ord("1")
                    if nums[idx]:
                        return False
                    nums[idx] = True
            return True


        def valid_box(start_row, start_col):
            nums = [False] * 9

            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col+3):
                    if board[row][col].isdigit():
                        idx = ord(board[row][col]) - ord("1")
                        if nums[idx]:
                            return False
                        nums[idx] = True
            return True

        for i in range(len(board)):
            curr_row, curr_col = (i //3) * 3, (i % 3) * 3 
            if not valid_row(i) or not valid_col(i) or not valid_box(curr_row, curr_col):
                return False

        return True

        