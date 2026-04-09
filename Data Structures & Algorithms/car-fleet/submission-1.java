class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        /**
            (target - positon[i]) / speed[i]) how long will the car take to reach the target
            [3,4,10,3]
            //if a car reaches the target faster than or equal another car than its a fleet
            
        **/
        int[][] pair = new int[position.length][2];
        Stack<Double> stack = new Stack<>();

        for(int i = 0; i < position.length; i++){
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }
        //Compares the first element of the two array
        Arrays.sort(pair, (a, b) -> Integer.compare(b[0], a[0]));

        for(int[] p : pair){
            stack.push((double)(target-p[0])/p[1]);
            if(stack.size() >= 2 && stack.peek() <= stack.get(stack.size()-2)){
                stack.pop();
            }
        }
        return stack.size(); 
    }
}
