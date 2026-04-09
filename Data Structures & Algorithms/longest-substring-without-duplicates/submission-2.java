class Solution {
    public int lengthOfLongestSubstring(String s) {
        /**
            you need a hashmap to keep track of the duplicates
            two pointer for the sliding window algo

            keep tracking the comparing for the max until you hit
            a duplicate if so
                move your left pointer plus one from the value given 
                by the hashmap for that character

        **/
        if(s.length() == 0) return 0;

        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0;
        int longestSub = 0;

        for(int right = 0; right < s.length(); right++){
            if(map.containsKey(s.charAt(right))){
                left = Math.max(map.get(s.charAt(right))+ 1, left);
            }
            map.put(s.charAt(right), right);
            longestSub = Math.max(longestSub, right - left + 1);
        }


        return  longestSub;

    }
}
