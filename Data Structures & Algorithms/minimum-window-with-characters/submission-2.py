class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count, window = {}, {}
        res, resLen = [-1, -1], float("infinity")


        for char in t:
            count[char] = count.get(char, 0) + 1

        have, need = 0, len(count)

        left = 0
        for right in range(len(s)):
            key = s[right]
            window[key] = window.get(key, 0) + 1

            if key in count and window[key] == count[key]:
                have+= 1

            while(have == need):
                length = right - left + 1
                if length < resLen:
                    resLen = length
                    res = [left, right]

                currKey = s[left]
                window[currKey] = window.get(currKey, 0) - 1

                if currKey in count and window[currKey] < count[currKey]:
                    have -= 1

                left += 1


        return s[res[0]:res[1]+1] if float("infinity") != resLen else ""
            
            
                

        