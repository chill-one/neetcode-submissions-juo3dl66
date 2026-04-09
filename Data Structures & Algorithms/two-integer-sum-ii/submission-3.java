class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /**
            Sorted in ascending order
            for res idx1 < idx2 and we are returing a list with two value
            idx1 != idx2
            start left 
            start right 
            move the right pointer if sum > target 
            move the left pointer if sum < target
        **/

        int ptr1 = 0;
        int ptr2 = numbers.length - 1;

        while(ptr1 < ptr2){
            int sum = numbers[ptr1] + numbers[ptr2];
            if(sum < target){
                ptr1++;
            }else if(sum > target){
                ptr2--;
            }else{
                return new int[]{ptr1+1,ptr2+1};
            }
        }

        return null;
    }
}
