class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;
        int maxArea = 0;

        while(l < r){
            int minVal = Math.min(heights[l], heights[r]);
            int area = minVal * (r-l);
            maxArea = Math.max(area, maxArea);

            if(heights[l] < heights[r]){
                l++;
            }else if(heights[r] < heights[l]){
                r--;
            }else{
                l++;
                r--;
            }
        }

        return maxArea;
    }
}
