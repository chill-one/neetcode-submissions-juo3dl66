class Solution {
    public boolean isPalindrome(String s) {
        /**
            introduce two pointer l and r
            loop from left and right to compare the char in the string
            if the char is not alph char than skip them for both l and r
            go unil l < r
        **/
        int l = 0;
        int r = s.length() - 1;

        while(l < r){
            while(l < r && !alphaNum(s.charAt(l))) l++;
            while(r > l && !alphaNum(s.charAt(r))) r--;
            if(l > r) return true;
            char leftChar = Character.toLowerCase(s.charAt(l));
            char rightChar = Character.toLowerCase(s.charAt(r));
            if(leftChar != rightChar){
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }
}
