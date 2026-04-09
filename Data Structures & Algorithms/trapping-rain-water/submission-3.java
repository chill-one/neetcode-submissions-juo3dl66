class Solution {
    public int trap(int[] height) {

        /**
        int[] maxR = new int[height.length];
        int[] maxL = new int[height.length];
        
        int maxl = height[0];
        int maxr = height[height.length-1];
        for(int i = 1; i < height.length; i++){
            maxL[i] = maxl = Math.max(maxl, height[i]);
        }

        for(int i = height.length-2; i >=0; i--){
            maxR[i] = maxr = Math.max(maxr, height[i]);
        }

        int water = 0;
        int math = 0;
        for(int i  = 0; i < height.length; i++){
            math = Math.min(maxL[i],maxR[i]) - height[i];
            if(math > 0){
                water += math;
            }
        }

        return water;
    }
    **/

        int l = 0; int r = height.length - 1;
        int maxLeft = height[l]; int maxRight = height[r];
        int water = 0;
        int sum = 0;

        while(l < r){
            if(height[l] <= height[r]){
                l++;
                maxLeft = Math.max(maxLeft, height[l]);
                sum = maxLeft - height[l];
                water += (sum > 0) ? sum : 0;

            }else{
                r--;
                maxRight = Math.max(maxRight, height[r]);
                sum = maxRight - height[r];
                water += (sum > 0) ? sum : 0;
            }
            
        }

        return water;
    }
        
}
