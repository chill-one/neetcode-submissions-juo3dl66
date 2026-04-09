class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /*
            introduce a hashmap with a string key and arraylist for value
            alph[26]-> some pattern 101....1.. turn this to string
            if this pattern is in hashmap append it to that if not create a new section
            loop throught the whole array
            use a built in function to get all the list
            #0#10#10000000000000000000000
            #01010000000000000000000000
        */
        HashMap<String,List<String>> map = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            String key = patternFinder(strs[i]);
            List<String> values = map.get(key);
            if(values != null){
                map.get(key).add(strs[i]);
            }else{
                List<String> val = new ArrayList<>();
                val.add(strs[i]);
                map.put(key,val);
            }
        }

        return new ArrayList<List<String>>(map.values());
    }

    private String patternFinder(String str){
        int[] arr = new int[26];
        for(int i = 0; i < str.length(); i++){
            arr[str.charAt(i) - 'a']++;
        }
        StringBuilder res = new StringBuilder();
        for(int i = 0; i < arr.length; i++){
            res.append("#");
            res.append(arr[i]);
        }
        return res.toString();
    }
}
