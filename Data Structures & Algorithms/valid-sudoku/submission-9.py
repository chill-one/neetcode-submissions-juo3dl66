class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        sub_section = defaultdict(set)


        for i in range(len(board)):
            for j in range(len(board[i])):
                print(i//3, j//3)
                val = board[i][j]
                if val == ".":
                    continue
                if val in col[j] or val in row[i] or board[i][j] in sub_section[(i // 3, j // 3)]:
                    return False


                col[j].add(val)
                row[i].add(val)
                sub_section[(i//3, j//3)].add(val)


        return True