class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = [0 for _ in range(26)]
        seen2 = [0 for _ in range(26)]

        for char in s:
            idx = ord(char) - ord('a')
            seen1[idx] += 1

        for char in t:
            idx = ord(char) - ord('a')
            seen2[idx] += 1

        return seen1 == seen2