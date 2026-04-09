class Solution {
    public boolean isValid(String s) {
        /**
            You have to use a stack as 
            the parentheses work in a manner where
            the middle parentheses must end first before any other parenthese
            to be valid

            first loop throught the string s where s[i] must have 
            a match by the end of the string s if it dosent this is
            not a valid parentheses

            s[i] if its a opening parantheses and the next closing 
            paranthese isnt the same as s[i] than its not a valid parentheses
        **/
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            switch(s.charAt(i)){
                case '[':
                    stack.add(']');
                    break;
                case '(':
                    stack.add(')');
                    break;
                case '{':
                    stack.add('}');
                    break;
                case ']':
                    if(stack.size() == 0 || stack.pop() != ']') return false;
                    break;
                case ')':
                    if(stack.size() == 0 ||stack.pop() != ')') return false;
                    break;
                case '}':
                    if(stack.size() == 0 || stack.pop() != '}') return false;
                    break;
            }
        }
        return (stack.size() == 0) ? true : false;
    }
}
