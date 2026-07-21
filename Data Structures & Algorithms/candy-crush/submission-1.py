class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        1) look for vertical , horizontall cursh
            if more than 3 same number -> mark them -1
            dic to keep track of the index
        2) Crush all the candies
        3) move all the candies to the bottom
        4) check if more candies to crush
        5) if thier is more respeat from step 1 else return the board
        """
        R,C = len(board),  len(board[0])

        def find_crush():
            found = False
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == 0:
                        continue
                    if c + 2 < C and abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]):
                        board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                        found = True

                    if r + 2 < R and abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]):
                        board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                        found = True

            return found

        while find_crush():
            for c in range(len(board[0])):
                a = len(board) - 1
                for r in range(len(board)-1, -1, -1):
                    if board[r][c] > 0:
                        board[a][c] = board[r][c]
                        a-=1

                while a >= 0:
                    board[a][c] = 0
                    a -= 1

        return board


                
                

            

            
        


