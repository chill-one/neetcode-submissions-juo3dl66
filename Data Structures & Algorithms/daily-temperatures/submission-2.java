class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        /**
            [1,4,1,2,1,0,0] <- res
            [5,6,] <- stack
            [30,38,30,36,35,40,28]
                             i 
            if the stack is not empty
                while(tempertaures[stack.peek()] < temepratures[i])
                    int idx = stack.pop()
                    res[idx] = i - idx;


            add the current idx to the list


        **/
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[temperatures.length];

        for(int i = 0; i < temperatures.length; i++){
            if(!stack.isEmpty()){
                while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                    int idx = stack.pop();
                    res[idx] = i - idx;
                }
            }
            stack.push(i);
        }

        return res;
    }
}
