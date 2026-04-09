class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /**
            use a data structure called dequeu which can
            get the element form the front and back in O(1)

            need left and right pointer

            use the formula n - k +1 to determine the size of the res array

            loop throught the array and keep adding to the dequeu 
                while deeque is not empty:
                    if the last elment is less than current value at right remove
                    and keep on doing this until the value at deeque is greater than right value


                add the value to deeque

                if(right - left + 1 == k) than add the value at front of deque to the res arrray
                and remove the ront of the deque 


            reuturn the array
             
        **/

        Deque<Integer> dq = new  LinkedList<>();
        int n = nums.length;
        int[] res = new int[n - k + 1];

        int left = 0;

        for(int right = 0; right < nums.length; right++){
            while(!dq.isEmpty() && nums[dq.getLast()] < nums[right]){
                dq.removeLast();
            }

            dq.addLast(right);

            if(dq.getFirst() < left){
                dq.removeFirst();
            }

            if((right + 1) >= k){
                res[left++] = nums[dq.getFirst()];
            }
            
        }
        return res;
    }
}
