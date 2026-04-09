class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        left = 0
        longest_substring = 0
        for right in range(len(s)):
            char = s[right]
            if char in dic:
                left = max(left, dic[char] + 1)
            dic[char] = right
            longest_substring = max(right - left + 1, longest_substring)

        return longest_substring


