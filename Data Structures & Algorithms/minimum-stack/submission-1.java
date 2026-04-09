class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        if(stack.isEmpty()){
            minStack.push(val);
        }else if(minStack.peek() > val){
            minStack.push(val);
        }else{
            minStack.push(minStack.peek());
        }

        stack.push(val);
    }
    
    public void pop() {
        if(stack.isEmpty() || minStack.isEmpty()) return;
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        if(stack.isEmpty()) return -1; 
        return stack.peek();
    }
    
    public int getMin() {
        if(minStack.isEmpty()) return -1;
        return minStack.peek();
    }
}
