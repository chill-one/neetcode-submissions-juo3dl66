class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        Scount = [0] * 26
        Tcount = [0] * 26

        for i in range(len(s)):
            Scount[ord(s[i]) - ord('a')] += 1
            Tcount[ord(t[i]) - ord('a')] += 1


        return Scount == Tcount

        