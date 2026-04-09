class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer,Boolean> previousInt = new HashMap<>();
        int maxCount = 0;
        for(int num : nums){
            int count = 1;
            if(!previousInt.containsKey(num))previousInt.put(num, true);

            int low = 1;
            while(previousInt.containsKey(num-(low++))) count++;

            int high = 1;
            while(previousInt.containsKey(num+(high++)))count++;

            maxCount = Math.max(count, maxCount);
            }
        return maxCount;
    }
}

