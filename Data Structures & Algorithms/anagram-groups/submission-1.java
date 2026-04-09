class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            String sortedStr = sortString(strs[i]);
            if(map.containsKey(sortedStr)){
                map.get(sortedStr).add(strs[i]);
            }else{
                List<String> list = new ArrayList<>();
                list.add(strs[i]);
                map.put(sortedStr,list);
            }
        }
        List<List<String>> valuesList = new ArrayList<>(map.values());
        return valuesList;
    }


    private String sortString(String str){
        char tempArray[] = str.toCharArray();
        Arrays.sort(tempArray);
        String sortedString = new String(tempArray);
        return sortedString;
    }
}
