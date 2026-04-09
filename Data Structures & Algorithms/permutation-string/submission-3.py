class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0  for i in range(26)]
        curr_window = [0 for i in range(26)]


        for char in s1:
            freq[ord(char) - ord('a')] += 1


        left = 0
        for right in range(len(s2)):
            curr_window[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 < len(s1):
                continue
            
            if curr_window == freq:
                return True

            curr_window[ord(s2[left]) - ord('a')] -= 1
            left += 1

        return False



    



        