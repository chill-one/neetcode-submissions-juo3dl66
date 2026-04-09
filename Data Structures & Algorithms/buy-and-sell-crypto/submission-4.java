class Solution {
    public int maxProfit(int[] prices) {
        /**
            have two pointers
            move the left pointer if the right is less than left else
            move right if its greater than equal too
        **/


        int maxProfit = 0;
        int left = 0;
        for (int right = 1; right < prices.length; right++) {
            if (prices[right] > prices[left]) {
                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            } else {
                left = right;
            }
        }

        return maxProfit;
    }
}
