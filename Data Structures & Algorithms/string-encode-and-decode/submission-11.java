class Solution {
    /**
        For each string add a indicator(speical char),the length of
        the string and the string itself
        Do this for every string


        look for the special character and if their is a number
        after the speical character using that number (number can be more than one character) loop until you 
        found all the char for that respective string

        Put them in an array
        
        2#we3#say1#:3#yes10#!@#$%^&*()
    **/

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();

        for(String s : strs){
            res.append(s.length());
            res.append("#");
            res.append(s);
        }

        return res.toString();
    }

    public List<String> decode(String str) {
        System.out.println(str);
        List<String> res = new ArrayList<>();

        for(int i = 0; i < str.length() - 1; i++){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int len = Integer.parseInt(str.substring(i,j));
            i = j + 1;
            j = i + len;
            res.add(str.substring(i, j));
            i = j - 1;
            }

        return res;
        }
    }

