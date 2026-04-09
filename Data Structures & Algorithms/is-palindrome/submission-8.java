class Solution {
    public boolean isPalindrome(String s) {
        int l = 0; int r = s.length()-1;
        if(s.length()<=1) return true;

        while(l < r){
            while(!isValid(s.charAt(l)) && l < r) l++;
            while(!isValid(s.charAt(r)) && l < r ) r--;

            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private boolean isValid(char c){
        return ((c>='A' && c<='Z') ||
                (c>='a' && c<='z') ||
                (c>='0' && c<='9'));
    }
}
