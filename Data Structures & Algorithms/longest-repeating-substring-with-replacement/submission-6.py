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
        
        dic = {}
        left = 0
        longest_sub = 0
        largest_count = 0

        for right in range(len(s)):
            key = s[right]
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
                
            largest_count = max(largest_count, dic[key])
            while((right - left + 1) - largest_count > k):
                dic[s[left]] -= 1
                left += 1

            longest_sub = max(right - left + 1, longest_sub)

        return longest_sub




            

        