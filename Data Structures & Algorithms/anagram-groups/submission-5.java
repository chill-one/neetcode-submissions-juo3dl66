class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            int[] count = new int[26];
            
            for(int j = 0 ; j < strs[i].length(); j++){
                count[strs[i].charAt(j) - 'a']++;
            }

            StringBuilder str = new StringBuilder();
            for(int k = 0; k < 26; k++){
                //You need a certain kind of mark to distingiush 
                // between key which may have similer numbers 
                // such as ["bdddddddddd","bbbbbbbbbbc"]
                //010100000000000000000000000
                //010100000000000000000000000
                //both string proudce the same counts but they are
                //not anagram so u need to put a mark in between count
                str.append(count[k]);
                str.append(',');
            }

            String key = str.toString();
            System.out.println(key);
            if(!map.containsKey(key)){
               map.put(key, new ArrayList<>());
            }

            map.get(key).add(strs[i]);
        }

        List<List<String>> valuesList = new ArrayList<>(map.values());
        return  valuesList ;
    }
}   
