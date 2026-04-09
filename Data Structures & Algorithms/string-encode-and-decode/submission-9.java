class Solution {

    public String encode(List<String> strs) {
        StringBuilder encodeStr = new StringBuilder();
        for(String s : strs){
            int len = s.length();
            encodeStr.append(len);
            encodeStr.append("#");
            encodeStr.append(s);
        }
        return encodeStr.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        for(int i = 0; i < str.length(); i++){
            int j = i;
            while(str.charAt(j) != '#'){j++;}

            int len = Integer.parseInt(str.substring(i,j));
            String res = str.substring(j+1,j+len+1);
            strs.add(res);
            i = j + len;
        }
        return strs;
    }
}
