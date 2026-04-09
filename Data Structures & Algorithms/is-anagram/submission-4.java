class Solution {
    public boolean isAnagram(String s, String t) {
        /*
            racecar
            carrace
            26 letters in a alph arr[26] 
            i is given by s[i]-'a'
            j is givne by t[i] -'a'
            In arr[i] increment by 1 
            in arr[j] decrement by 1
            loop until the end of the array

            loop the arr if arr[i] != 0 than return false
            else return true
        */
        if(s.length() != t.length()) return false;

        int[] arr = new int[26];
        for(int i = 0; i < s.length(); i++){
            arr[s.charAt(i)-'a']++;
            arr[t.charAt(i)-'a']--;
        }

        for(int i = 0; i < arr.length; i++){
             if(arr[i] != 0) return false;
        }

        return true;
    }
}
