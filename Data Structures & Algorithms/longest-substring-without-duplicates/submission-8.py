class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Since thier is a possibility that you can go further back than your current left pointer
        #Use hashmap to keep track of the index you were at


        dic = {}
        max_ = 0

        left = 0

        for right in range(len(s)):
            key = s[right]
            if key in dic:
                left = max(dic[key] + 1, left)    
            dic[key] = right
            max_ = max(right - left + 1, max_)

        return max_

        