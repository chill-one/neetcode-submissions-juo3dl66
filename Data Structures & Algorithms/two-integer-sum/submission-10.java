class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> prevElement = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int y = target - nums[i];
            if(prevElement.get(y) != null ){
                return new int[]{prevElement.get(y), i};
            }else{
                prevElement.put(nums[i], i);
            }
        }

        return null;
    }
}
