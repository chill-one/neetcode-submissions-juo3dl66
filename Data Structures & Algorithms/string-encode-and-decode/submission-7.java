class Solution {

    public String encode(List<String> strs) {
        if(strs.size()==0){return "";}
        StringBuilder string = new StringBuilder();
        for(String str : strs){
            int len = str.length();
            string.append(len);
            string.append("#");
            string.append(str);
        }
        return string.toString();
    }

    public List<String> decode(String s) {
        if(s.length()==0){return new ArrayList<>();}

        List<String> res = new ArrayList<>();
        int len = s.length(), i = 0, j, slen;
        while(i < len){
            j = i;
            while(s.charAt(j)!='#'){
                j++;
            }
            slen = Integer.parseInt(s.substring(i,j));
            res.add(s.substring(j+1,slen+j+1));
            i = j + slen + 1;
        }
      return res;
    }
}      
