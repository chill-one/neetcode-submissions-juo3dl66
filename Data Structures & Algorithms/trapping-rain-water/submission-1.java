class Solution {
    public int trap(int[] height) {
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
}
