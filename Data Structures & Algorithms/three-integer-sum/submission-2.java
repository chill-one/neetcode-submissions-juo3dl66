class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for(int i = 0 ; i < nums.length; i++){
            if(nums[i] > 0) break;
            if(i > 0 && nums[i - 1] == nums[i]) continue;
            int l = i + 1;
            int r = nums.length - 1;

            while(l < r){
                if(nums[i] + nums[l] + nums[r] == 0){
                    List<Integer> triplets = new ArrayList<>();
                    triplets.add(nums[i]);
                    triplets.add(nums[l]);
                    triplets.add(nums[r]);
                    res.add(triplets);
                    l++;
                    r--;
                    while(nums[l] == nums[l-1] && l < r) l++;

                }else if(nums[i] + nums[l] + nums[r] < 0){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return res;
    }
}
