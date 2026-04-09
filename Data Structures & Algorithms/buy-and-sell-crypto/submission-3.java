class Solution {
    public int maxProfit(int[] prices) {
        /**
            have two pointers
            move the left pointer if the right is less than left else
            move right if its greater than equal too
        **/


        int maxProfit = 0;
        int left = 0;
        int right = 1;

        while (left < prices.length && right < prices.length){
            maxProfit = Math.max(maxProfit, prices[right] -  prices[left]);
            if(prices[right] < prices[left]){
                left++;
            }else{
                right++;
            }
        }

        return maxProfit;
    }
}
