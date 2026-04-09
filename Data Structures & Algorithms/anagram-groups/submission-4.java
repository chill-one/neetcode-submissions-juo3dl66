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
                str.append(',');
                str.append(count[k]);
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
