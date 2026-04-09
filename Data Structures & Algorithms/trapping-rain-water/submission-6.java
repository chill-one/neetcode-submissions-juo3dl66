class Solution {
    public int trap(int[] height) {
        /**
            need two pointer at each ends
            maxLeft store the left max
            maxRight store the right max

            move when l maxLeft is less than maxRight else move R if not maxRight
            check if you need to update the maxLeft or maxRight when thier
            respective pointer is moved.
            than add to area if localArea > 0 else dont add
            

        **/       
        int l = 0;
        int r = height.length-1;
        int maxLeft = height[l];
        int maxRight = height[r];
        int area = 0;
        while(l < r){
            if(maxLeft < maxRight){
                l++;
                maxLeft = Math.max(maxLeft, height[l]);
                area += Math.max(maxLeft - height[l], 0);
            }else {
                r--;
                area += Math.max(maxRight - height[r], 0);
                maxRight = Math.max(maxRight, height[r]);
            }
        } 
        return area;
    }
}
