class Solution {
    public int characterReplacement(String s, int k) {
        if(s.length() == 0) return 0;
        /**
            WE need two pointers to do the sliding windo algo
            another variable to keep track of the longest with replacement
            a temp variable for k
            Need a hashMap to keep track of where we started our replacement

            loop until the end of the array
                if our subString_length - count[character] gives how many replacement you need to do
                    change our left pointer to the value stored at hashMap
                    with the key 

            ABABBA
        **/
        int left = 0;
        int maxFreq = 0;
        int res = 0;
        int n = s.length();

        HashMap<Character, Integer> map = new HashMap<>();

        for(int right = 0; right < s.length(); right++){
            char key = s.charAt(right);
            map.put(key, map.getOrDefault(key, 0) + 1);
            maxFreq = Math.max(map.get(key), maxFreq);
            while((right - left + 1) - maxFreq > k){
                map.put(s.charAt(left),map.get(s.charAt(left)) - 1);
                left++;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}
