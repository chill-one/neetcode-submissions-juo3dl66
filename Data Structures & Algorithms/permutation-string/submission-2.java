class Solution {
    public boolean checkInclusion(String s1, String s2) {
        /**
        To solve this efficiently, the code uses the idea that if two strings are permutations of each other, 
        they must have the exact same character counts.

        So instead of checking every substring one by one (which would be slow), the code:

        Counts how many times each letter appears in s1.
        Then, it looks at the first window (same length as s1) in s2 and counts those characters too.
        If the character counts match exactly, we found a valid permutation.
        After that, the code slides a window across s2, one character at a time:

        It adds the new character on the right of the window.
        It removes the character that's no longer in the window (from the left).
        It keeps track of how many letters still match between s1 and the current window in s2.
        If at any point all 26 letter counts match, it means that a permutation of s1 exists somewhere in s2, so it returns true.

        If the loop finishes and no match is found, it returns false.
        **/
        if (s1.length() > s2.length()) {
            return false;
        }

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];

        // Create two array with the character counts of the s1 in both s1 and s2
        for(int i = 0; i < s1.length(); i++){
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        // Go throught both array check how many matches we currently have 
        int matches = 0;
        for(int i = 0; i < 26; i++){
            if(s1Count[i] == s2Count[i]){
                matches++;
            }
        }

        //we have two pointer: left pointer starts at 0 while right pointer starts at the lenght of our s1 
        int l = 0;
        for(int r = s1.length(); r < s2.length(); r++){
            // if we have the same amount of matches that means we have a permutation in the array of s1
            if(matches == 26){
                return true;
            }
            
            //Moving our window up 

            //Increase our right counter
            int index = s2.charAt(r) - 'a';
            s2Count[index]++;
            //compare if we have same counter at that idx
            if(s1Count[index] == s2Count[index]){
                matches++;
            //compare if we have more count than we need
            }else if (s1Count[index] + 1 == s2Count[index]){
                matches--;
            }
            //decrease our left counter
            index = s2.charAt(l) - 'a';
            s2Count[index]--;
            //compare if we have same counter at that idx
            if (s1Count[index] == s2Count[index]) {
                matches++;
            //compare if we have less count than we need
            } else if (s1Count[index] - 1 == s2Count[index]) {
                matches--;
            }
            //move our l so we can get to the next substring 
            l++;
        }
        return matches == 26;
    }
}
