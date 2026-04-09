class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int preFix[] = new int[len];
        int postFix[] = new int[len];
        preFix[0] = postFix[len-1] = 1;

        //[1,2,8,48]
        //[2,8,24,6]
        for(int i = 1; i < len; i++){
            preFix[i] = preFix[i-1] * nums[i-1];
        }

        for(int i = len - 2; i >= 0 ; i--){
            postFix[i] = postFix[i+1]*nums[i+1];
        }

        int res[] = new int[len];
        for(int i = 0 ; i < len; i++){
            res[i] = preFix[i] * postFix[i];
        }

        return res;
    }
}  
