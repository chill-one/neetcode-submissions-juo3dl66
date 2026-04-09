class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /**
            need a set, 3 pointer
            need to sort the array first
            than itterat one pointer linearly
            you use 2 pointer one at the back and one at the front
            if nums[i] + nums[l] + nums[r] > 0 r--
              nums [i] + nums[l] + nums[r] < 0 l++

            keep track of the 3 values in a list
        **/

        int[] sortedNums = new int[nums.length];
        System.arraycopy(nums, 0, sortedNums, 0, nums.length);
        Arrays.sort(nums);
        int l;
        int r;
        int sum;
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < nums.length-2; i++){
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            l = i+1;
            r = nums.length-1;
            while(l < r){
                sum = nums[i] + nums[l] + nums[r];
                if(sum < 0){
                    l++;
                }else if(sum > 0){
                    r--;
                }else{
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[l]);
                    triplet.add(nums[r]);
                    res.add(triplet);
                    r--;
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }

            }

        }

        return res;
    }
}
