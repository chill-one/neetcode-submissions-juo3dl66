class MinStack {
    /**
        we need two stacks 
            normal stack is to keep track of all the values
            min stack is to keep track of the most min element at
            each value of our stack
        
        Tricky part is if we have a duplicate min num which is 0 our stakcs
        look like [0,1,0] than we remove 0 our min stil needs to be 0 at the value 1.
    **/
    class Value{
        int val;
        int minVal;
        public Value(int val, int minVal){
            this.val = val;
            this.minVal = minVal;
        }
    }
    Stack<Value> stack;


    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if(stack.isEmpty()){
            stack.add(new Value(val, val));
        }else{
            stack.add(new Value(val, Math.min(val,stack.peek().minVal)));
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek().val;
    }
    
    public int getMin() {
        return stack.peek().minVal;
    }
}
