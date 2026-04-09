class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        /**
        Their is a col number of element in matrix[i] for a 2d matrix
        so using (r/col) tells me which row my current element is on.
        As for (col % Col) it tells me which column would this element be on.
        midRow = r / Col;
        midCol = col % COL; // 2 / 3 = 0
        **/ 
        int COL = matrix[0].length;
        int ROW = matrix.length;

        int l = 0;
        int r = COL * ROW - 1;
        
        while(l <= r){
            int mid = l + (r - l) / 2;
            int midRow = mid/COL;
            int midCol = mid%COL;
            int val = matrix[midRow][midCol];

            if(val < target){
                l = mid + 1;
            }else if (val > target){
                r = mid - 1;
            }else{
                return true;
            }
        }

        return false;
    }
}
