class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Since thier is a possibility that you can go further back than your current left pointer
        #Use hashmap to keep track of the index you were at

        dic = {}
        longest_sub = 0
        left = 0

        for right in range(len(s)):
            key = s[right]
            
            if key in dic:
                left = max(left, dic[key] + 1)

            dic[key] = right
            longest_sub = max(longest_sub, right - left + 1)


        return longest_sub
        