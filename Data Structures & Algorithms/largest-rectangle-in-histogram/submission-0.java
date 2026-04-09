class Solution {
    public int largestRectangleArea(int[] heights) {
        
        /**
            [2,1,5,6,2,3]
            If heights arent in increasing order we need to pop it 
            as its the heights that has reached its limit 

            have a stack
            have a variable to keep track of the max value

            loop throught the heights 
                keep adding to the stack until heights[i] < stack head
                    loop unil either our stack is empty or heights[i] > stack head
                        pop the value from the stack which is an idx
                        grab the value from heights[idx]
                        get the width using (i - idx)
                        get the height using height[idx]
                        area = widht * height;
                        maxVal = Math.max(maxVal, area);
            
            return maxval

        **/

        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;

        for(int i = 0; i <= heights.length; i++){
            while(!stack.isEmpty() &&   (i == heights.length || heights[stack.peek()] >= heights[i])){
                int idx = stack.pop();
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                int area = width * heights[idx];
                maxArea = Math.max(area, maxArea);
            }   
            stack.push(i);
        }

        return maxArea;
        //[2,1,5,6,2,3]
        /**
            maxVal: 10
            i: 5
            stack : 5,4,1
        **/

    }
}
