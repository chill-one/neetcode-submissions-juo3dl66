class Solution {
    public int[] productExceptSelf(int[] nums) {
        /** 
             [1,2,4,6]
             [1,1,2,8] 
             [48,24,6,1] 
             [48,24,12,8]
        **/

        int[] preFex = new int[nums.length];
        preFex[0] = 1;

        for(int i = 1; i < nums.length; i++){
            preFex[i] = preFex[i - 1] * nums[i - 1];
        }

        int temp = 1;
        for(int i = nums.length - 1; i >= 0; i--){
            preFex[i] = temp * preFex[i];
            temp *= nums[i];
        }

        return preFex;
        
    }
}  
