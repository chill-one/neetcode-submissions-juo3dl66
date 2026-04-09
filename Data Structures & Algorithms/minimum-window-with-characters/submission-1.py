class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, count = {}, {}

        res, reslen = [-1,-1],float("infinity")

        left = 0
        for char in t:
            count[char] = count.get(char, 0) + 1

        have, need = 0, len(count)
        for right in range(len(s)):
            key = s[right]
            window[key] = window.get(key, 0) + 1

            #You only add when the value at both window and count are equal to each other
            if key in count and count[key] == window[key]:
                have += 1

            while(have == need):
                if(right - left + 1 < reslen):
                    res = [left, right]
                    reslen = right - left + 1

                key = s[left]
                window[key] = window.get(key, 0) - 1
                #we should only decriment have if and only if widow value for key is less than what we need 
                if key in count and window[key] < count[key]:
                    have -= 1
                left += 1

        return s[res[0]:res[1]+1] if float("infinity") != reslen else ""

            
            
                

        