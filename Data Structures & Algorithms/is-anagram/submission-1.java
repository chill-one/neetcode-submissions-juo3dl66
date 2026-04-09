class Solution {
    public boolean isAnagram(String s, String t) {
        int[] container = new int[26];

        for(int i = 0; i < s.length(); i++){
            container[s.charAt(i)-'a']++;
        }

        for(int i = 0; i < t.length(); i++){
            container[t.charAt(i)-'a']--;
        }

        for(int i = 0; i< container.length; i++){
            if(container[i]!=0) return false;
        }

        return true;
    }
}
