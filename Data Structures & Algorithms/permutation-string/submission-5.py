class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False


        left = 0
        freq = [0] * 26
        expected = [0] * 26

        for char in s1:
            expected[ord('a') - ord(char)] += 1


        for right, char  in enumerate(s2):
            freq[ord('a') - ord(char)] += 1
            if right - left + 1 < n:
                continue

            if freq == expected:
                return True

            left_char = s2[left]
            freq[ord('a') - ord(left_char)] -= 1
            left += 1


        return False





        

            

