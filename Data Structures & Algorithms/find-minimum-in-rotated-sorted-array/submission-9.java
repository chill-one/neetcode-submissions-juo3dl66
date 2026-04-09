class Solution {
    public int findMin(int[] nums) {
        /**
            0  1. 2. 3. 4. 5
            [3, 4, 5, 6, 1, 2]
             l     m       r

             //if our nums[mid] > nums[l] && nums[l] < nums[r]
                record your cuurent nums[m]
                shift your right pointer to the middle
            // if our nums[mid] > nums[r] && nums[l] > nums[r]
                recourd your crrent nums [m]
                shift your left pointer up

            have a left pointer
            have a right pointer
            keep track of the current min value

            loop while left <= right
                mid = left + (right - left) / 2

             0  1. 2. 3
            [4, 5, 6, 7]
             l  r             
            
            l: 0
            r: 3
            m: 1
        **/

        int l = 0;
        int r = nums.length - 1;
        int min = Integer.MAX_VALUE;

        while(l <= r){
            int mid = l + (r - l) / 2;
            if(nums[l] <= nums[r]){
                min = Math.min(min,nums[l]);
                l++;
                r--;
            }
            else if(nums[mid] >= nums[l]){
                l = mid + 1;
            }else{
                r = mid - 1;
            }
            min = Math.min(min,nums[mid]);
        }

        return min;
    }
}
