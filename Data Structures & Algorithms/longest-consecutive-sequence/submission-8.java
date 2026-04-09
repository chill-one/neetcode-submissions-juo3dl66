class Solution {
    public int longestConsecutive(int[] nums) {
        /**
            Add all the elements into the hash set
            for each number keep interating forward and back ward until elements is not in set
            keep track of the highest consecative number

        **/
        if(nums.length == 1) return 1;

        Set<Integer> set = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }

        int longestConst = 0;
        for(int i = 0; i < nums.length; i++){
            int incrementUp = nums[i]++;
            int localLongestConst = 0;
            while(set.contains(incrementUp)){
                incrementUp++;
                localLongestConst++;
            }
            if(localLongestConst > longestConst){
                longestConst = localLongestConst;
            }

        } 
        return longestConst; 
    }
}
