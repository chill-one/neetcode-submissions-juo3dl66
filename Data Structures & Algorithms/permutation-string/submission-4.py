class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = self.getCount(s1)
        s2_count = [0 for i in range(26)]
        left = 0

        for right in range(len(s2)):
            s2_count[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 < len(s1):
                continue
            
            if s2_count == s1_count:
                return True
            else:
                s2_count[ord(s2[left]) - ord('a')] -= 1
                left+=1
        return False

    def getCount(self, s):
        count = [0 for i in range(26)]

        for idx in range(len(s)):
            char = s[idx]

            count[ord(char) - ord('a')] += 1

        return count