class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < board.length; i++){
            if(!isValidCol(board,i)) return false;
            if(!isValidRow(board,i)) return false;
        }
        for(int i = 0; i < board.length; i+=3){
            for(int j = 0; j < board.length; j+=3){
                if(!isValidSubBox(j,i,board)) return false;
            }
        }

        return true;
    }

    private boolean isValidSubBox(int row, int col, char[][] board){
        HashMap<Character, Boolean> hasAppeard = new HashMap<>();
        for(int i = row; i < (row+3); i++){
            for(int j = col; j < (col+3); j++){
                char val = board[i][j];
                if(val == '.') continue;
                if(hasAppeard.containsKey(val)){
                    return false;
                }
                hasAppeard.put(val,true);
            }
        }
        return true;
    }

    private boolean isValidCol(char[][] board, int row){
        HashMap<Character, Boolean> hasAppeard = new HashMap<>();
        for(int i = 0; i < board[row].length; i++){
            char val = board[i][row];
            if(val == '.') continue;
            if((val < 48 || val > 57) || hasAppeard.containsKey(val)){
                return false;
            }
            hasAppeard.put(val,true);
        }
        return true;
    }

        private boolean isValidRow(char[][] board, int col){
        HashMap<Character, Boolean> hasAppeard = new HashMap<>();
        for(int i = 0; i < board.length; i++){
            char val = board[col][i];
            if(val == '.') continue;
            if((val < 48 || val > 57)  || hasAppeard.containsKey(val)){
                return false;
            }
            hasAppeard.put(val,true);
        }
        return true;
    }
}
