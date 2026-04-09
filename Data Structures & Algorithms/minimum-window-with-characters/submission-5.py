class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        sub_count = {}

        left = 0
        have = 0
        for char in t:
            dic[char] = dic.get(char, 0) + 1

        resLen = float("infinity")
        start = 0
        for right in range(len(s)):
            char = s[right]
            
            if char in dic:
                sub_count[char] = sub_count.get(char, 0) + 1
                if sub_count[char] == dic[char]:
                    have+= 1

                while have == len(dic):
                    if right - left + 1 < resLen:
                        resLen = right - left + 1
                        start = left
                    char = s[left]
                    if char in sub_count:
                        sub_count[char] = sub_count.get(char, 0) - 1
                        if sub_count[char] < dic[char]:
                            have -= 1

                    left += 1
        return s[start: start + resLen] if resLen != float("infinity") else ""

                    
                

        