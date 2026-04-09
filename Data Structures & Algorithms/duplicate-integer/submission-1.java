class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> container = new HashSet<>();

        for( int num : nums){
            if(!container.add(num)) return true;
            container.add(num);
        }

        return false;
    }
}
