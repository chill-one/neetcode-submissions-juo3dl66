class Solution {
    public int evalRPN(String[] tokens) {
        /**
            create a stack which will keep track of the given number
            at tokens[i], 
            if tokens[i] is in [+,-,*,/] pop two numbers from
            the stack than do the respective opertaion on those numbers. 
            Add the result into the stack and keep on going until your at the end.

            After your out of the loop return the first elemnt in your stack
        **/
        Stack<Integer> prevNumber = new Stack<>();

        for(int i = 0; i < tokens.length; i++){
            switch(tokens[i]){
                case "+":
                    prevNumber.push(prevNumber.pop()+prevNumber.pop());
                    break;
                case "-":
                    int secondNumber = prevNumber.pop();
                    prevNumber.push(prevNumber.pop()-secondNumber);
                    break;
                case "*":
                    prevNumber.push(prevNumber.pop()*prevNumber.pop());
                    break;
                case "/":
                    int divisor = prevNumber.pop();
                    prevNumber.push(prevNumber.pop()/divisor);
                    break;
                default:
                    prevNumber.push(Integer.parseInt(tokens[i]));
            }
        }

        return prevNumber.pop();


    }
}
