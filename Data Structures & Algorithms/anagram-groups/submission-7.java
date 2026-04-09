class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(int i = 0 ; i < strs.length; i++){
            String freq = strFreq(strs[i]);
            map.putIfAbsent(freq, new ArrayList<>());
            map.get(freq).add(strs[i]);
        }

        List<List<String>> res = new ArrayList<>(map.values());
        return res;
    }

    private String strFreq(String str){
        int[] freq = new int [26];

        for(int i = 0; i < str.length(); i++){
            freq[str.charAt(i) - 'a']++;
        }

        return Arrays.toString(freq);
    }
}
