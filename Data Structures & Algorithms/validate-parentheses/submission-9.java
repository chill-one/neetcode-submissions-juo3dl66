class Solution {
    public boolean isValid(String s){
        if (s.length() % 2 != 0) return false;

        char[] stack = new char[s.length()];
        int position = 0;

        for(char character : s.toCharArray())
        {
            switch(character){
                
                case('('):
                    stack[position++] = ')';
                    break;
                case('['):
                    stack[position++] = ']';
                    break;
                case('{'):
                    stack[position++] = '}';
                    break;
                default:
                    position--;
                    if(position < 0 || character!=stack[position]){return false;}
                    break;
            }
        }

        return position==0;
    }
}
