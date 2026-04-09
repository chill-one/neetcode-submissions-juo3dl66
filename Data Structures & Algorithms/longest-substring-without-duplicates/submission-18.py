class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        dic = {}
        left = 0
        "yxxmty"
        for right, char in enumerate(s):
            if char in dic:
                left = max(dic[char] + 1, left)

            dic[char] = right
            longest = max(longest, right - left +1)


        return longest
                
