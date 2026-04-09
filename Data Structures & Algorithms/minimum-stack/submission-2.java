class MinStack {
    /**
        we need two stacks 
            normal stack is to keep track of all the values
            min stack is to keep track of the most min element at
            each value of our stack
        
        Tricky part is if we have a duplicate min num which is 0 our stakcs
        look like [0,1,0] than we remove 0 our min stil needs to be 0 at the value 1.
    **/
    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.add(val);
        if(minStack.isEmpty()){
            minStack.push(val);
        }else{
            minStack.push(Math.min(minStack.peek(), val));
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
