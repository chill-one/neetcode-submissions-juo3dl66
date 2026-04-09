class Solution {
    public String minWindow(String s, String t) {
        if(t.length() > s.length()) return "";

        /**
        s = OUZODYXAZV
            ZODYX , YXAZ
        have counter for have_counter and need_counter 
        one hash map for keeping track of the current char counter
        second hash map for keeping rack of the needed char counter
        res is an array lenght 2 
        alos a res_len

        have a left and right pointer 
        loop throught the string and mover the right pointer up
            if a s[right] is in the hashmap for needed char increase the current counter up for current hashmap
            also check if the char your currently has reached equall the count it needs if so increase the have counter
            while  if have_counter is equal to need_counter if so update the res and res_len with that remove the first char from the current hashmap and have_counter 
        **/

        int have_counter = 0;

        HashMap<Character, Integer> have_map = new HashMap<>();
        HashMap<Character, Integer> need_map = new HashMap<>();

        for(int i = 0; i < t.length(); i++){
            Character key = t.charAt(i);
            need_map.put(key, need_map.getOrDefault(key, 0) + 1);
        }
        int need_counter = need_map.size();

        int left = 0;
        int[] res = new int[2];
        int res_length = Integer.MAX_VALUE;

        for(int right = 0; right < s.length(); right++){
            Character key = s.charAt(right);
            //Only include keys that are in 
            if(need_map.containsKey(key)){ 
                have_map.put(key, have_map.getOrDefault(key, 0) + 1);
                if(have_map.get(key).equals(need_map.get(key)))
                    have_counter++;
            }
            while(have_counter == need_counter){
                int length = right - left + 1;
                if(length < res_length){
                    res_length = length;
                    res[0] = left;
                    res[1] = right;
                }

                key = s.charAt(left++);
                if(have_map.getOrDefault(key, 0) > 0){
                    have_map.put(key, have_map.getOrDefault(key, 0) - 1);
                    if(have_map.get(key) < need_map.get(key)){
                        have_counter--;
                    }
                }
            }
        }


        return (Integer.MAX_VALUE == res_length) ? "" : s.substring(res[0], res[1]+1);

    }
}
