class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        /**
            The main part of this question is recognizing that
            piles has to be less than equal to hours. 
            Knowing that k has to be between 1 and the max of 
            our piles is also needed

            get the max of the array
            us one as your low point

            using the max and low get a mid point and use that
            as your k keep doing this until you find the minmium integer


        **/

        int left = 1;
        int right = piles[0];
        //Gets the max
        for(int i = 1; i < piles.length; i++){
            right = Math.max(right, piles[i]);
        }
        int res = right;
        // 1 <= 2   k = 1
        while(left <= right){
            int totalTime = 0;
            int k = left + (right - left) / 2;
            for(int pile : piles){
                totalTime += Math.ceil((double) pile/k);
            } 
            if(totalTime > h){
                left = k + 1;
            }else if(totalTime <= h){
                res = Math.min(res, k);
                right = k - 1;
            }
        }

        return res;
    }
}
