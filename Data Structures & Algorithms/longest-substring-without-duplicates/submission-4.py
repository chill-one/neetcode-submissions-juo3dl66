class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        left = 0
        longest_sub = 0

        for right in range(len(s)):
            chararcter = s[right]
            if chararcter in dic:
                left = max(dic[chararcter] + 1, left)
                dic[chararcter] = right

            dic[chararcter] = right
            longest_sub = max(longest_sub, right - left + 1)

        return longest_sub
