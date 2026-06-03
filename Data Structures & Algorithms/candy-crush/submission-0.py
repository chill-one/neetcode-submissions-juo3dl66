class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed = True

        while crushed:
            #Find all the horozontal candies
            crushed = False
            for i in range(len(board)):
                for j in range(len(board[i])-2):
                    if board[i][j] == 0:
                        continue

                    val = abs(board[i][j])
                    if val == abs(board[i][j+1]) == abs(board[i][j+2]):
                        board[i][j] = board[i][j+1] = board[i][j+2] = -val
                        crushed = True

            #Find all the vertical candies
            for i in range(len(board[0])):
                for j in range(len(board)-2):
                    
                    if board[j][i] == 0:
                        continue

                    val = abs(board[j][i])
                    if val == abs(board[j+1][i]) == abs(board[j+2][i]):
                        board[j][i] = board[j+1][i] = board[j+2][i] = -val
                        crushed = True

            if crushed:
                #Turn the marked number to zero
                for i in range(len(board)):
                    for j in range(len(board[0])-1, -1, -1):
                        if board[i][j] < 0:
                            board[i][j] = 0

                #shift all the candiess down
                nonZero = []
                for c in range(len(board[0])):
                    nonZero = []
                    for r in range(len(board)):
                        if board[r][c] != 0:
                            nonZero.append(board[r][c])
                            board[r][c] = 0

                    for r in range(len(board)-1, -1, -1):
                        if nonZero:
                            board[r][c] = nonZero.pop()


        return board

            


                
                    






            