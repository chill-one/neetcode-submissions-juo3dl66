class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> previousInt = new HashSet<>();
        int maxCount = 0;
        for(int num : nums){
            int count = 1;
            previousInt.add(num);
            int low = 1;
            while(previousInt.contains(num-(low++))) count++;

            int high = 1;
            while(previousInt.contains(num+(high++)))count++;

            maxCount = Math.max(count, maxCount);
            }
        return maxCount;
    }
}

