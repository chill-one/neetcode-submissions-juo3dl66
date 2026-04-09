class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        section = defaultdict(set)


        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                curr_val = board[i][j]
                if curr_val in col[j] or curr_val in row[i] or curr_val in section[(i //3, j // 3)]:
                    return False


                col[j].add(curr_val)
                row[i].add(curr_val)
                section[(i//3, j//3)].add(curr_val)


        return True 