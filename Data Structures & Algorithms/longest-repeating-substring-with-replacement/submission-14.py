class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rep = longest = left = 0

        prevChar = defaultdict(int)

        for right, char in enumerate(s):

            prevChar[char] += 1
            rep = max(prevChar[char], rep)

            while right - left + 1 - rep > k:
                leftChar = s[left]
                prevChar[leftChar] -= 1
                left += 1

            longest = max(longest, right - left + 1)


        return longest



            

