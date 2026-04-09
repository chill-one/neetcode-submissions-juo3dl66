class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> row = new HashMap<>();
        HashMap<Integer, HashSet<Character>> col = new HashMap<>();
        
        for(int i = 0; i < board.length; i+=3){
            for(int j = 0; j < board.length; j+=3){
                if(!checkSection(board,i,j,row,col)){
                    return false;
                }
            }
        }
        return true;

    }

    public boolean checkSection(char[][] board, int start, int col, HashMap<Integer, HashSet<Character>> rowDup, HashMap<Integer, HashSet<Character>> colDup){
        HashSet<Character> dup = new HashSet<>();
        for(int i = start; i < start+3; i++){
            for(int j = col ; j < col+3; j++){
                if(board[i][j] == '.') continue;
                if(!dup.add(board[i][j])){
                    return false;
                }
                
                if(rowDup.get(i) != null && !rowDup.get(i).add(board[i][j])){
                    return false;
                }else if(rowDup.get(i) == null){
                    rowDup.put(i, new HashSet<>());
                    rowDup.get(i).add(board[i][j]);
                }

                if(colDup.get(j) != null && !colDup.get(j).add(board[i][j])){
                    return false;
                }else if (colDup.get(j) == null){
                    colDup.put(j, new HashSet<>());
                    colDup.get(j).add(board[i][j]);
                }
            }
        }
        return true;
    }
}
