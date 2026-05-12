class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLeft = 0
        maxPal = 1
        n = len(s)


        for i in range(n):
            left = i - 1
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > maxPal:
                    maxLeft = left
                    maxPal = right - left + 1
                left -= 1
                right += 1

            left = i - 1 
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > maxPal:
                    maxLeft = left
                    maxPal = right - left + 1
                left -= 1
                right += 1

        return s[maxLeft: maxLeft + maxPal ]