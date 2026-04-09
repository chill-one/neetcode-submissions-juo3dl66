class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) return 0;

        int max = Integer.MIN_VALUE;
        int lowBuy = prices[0];

        for(int i = 0; i < prices.length; i++){
            if(lowBuy > prices[i]){
                lowBuy = prices[i];
            }
            max = Math.max(prices[i] - lowBuy, max);
        }

        return (max > 0)? max : 0;
    }
}
