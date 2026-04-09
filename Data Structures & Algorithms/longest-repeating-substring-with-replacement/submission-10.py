class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_count = {}
        max_count = 0
        res = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            character_count[char] = character_count.get(char, 0) + 1
            max_count = max(max_count, character_count[char])

            while right - left + 1 - max_count > k:
                char = s[left]
                character_count[char] = character_count.get(char, 0) - 1
                left += 1

            res = max(right - left + 1, res)


        return res



    