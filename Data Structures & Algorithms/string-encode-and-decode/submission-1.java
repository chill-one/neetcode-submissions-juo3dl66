class Solution {

    public String encode(List<String> strs) {
        StringBuilder string = new StringBuilder();
        for(String str : strs){
            int len = str.length();
            string.append(len);
            string.append("#");
            string.append(str);
        }
        return string.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();

        for(int i = 0; i < str.length(); i++){
            StringBuilder len = new StringBuilder();
            for(int j = i; j < str.length(); j++){
                if(str.charAt(j) == '#'){
                    i = j;
                    break;
                }
                len.append(str.charAt(j));
            }
            int length = Integer.valueOf(len.toString());
            strs.add(str.substring(i+1, i+length+1));
            i += length ;
            }
        return strs;
        }
    }      
