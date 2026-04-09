class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
         HashMap<String, List<String>> res = new HashMap<>();

         for(String s : strs){
            int num[] = new int[26];
            for(char c : s.toCharArray()){
                num[c -'a']++;
            }
            String numString = Arrays.toString(num);
            res.putIfAbsent(numString, new ArrayList<>());
            res.get(numString).add(s);
         }
         return new ArrayList<>(res.values());
    }



    
}
