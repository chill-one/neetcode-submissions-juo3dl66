from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            To slove this you need to know the largest_count in your hashmap
            so keep track of it for each itteration

            largest_count allows us to know what the current replacement states is
            since right - left + 1 gives us the length of the string hence , 
            (right - left + 1) - largest_count must be less than equal to K
            for it to be valid substring

        """
        largest_count = 0
        dic = {}

        left = 0
        longest_sub = 0

        for right in range(len(s)):
            key = s[right]
            dic[key] = dic.get(key, 0) + 1
            largest_count = max(largest_count, dic[key])
            sub_string_length = right - left + 1

            while (right - left + 1 - largest_count) > k :
                left_key = s[left]
                dic[left_key]-= 1
                left += 1

            longest_sub = max(longest_sub, right - left + 1)
        
        return longest_sub
            

        