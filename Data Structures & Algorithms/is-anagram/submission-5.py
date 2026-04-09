class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False

        s_arr = [ 0 for i in range(26)]
        t_arr = [ 0 for i in range(26)]

        for s_char, t_char in zip(s, t):
            inital = ord('a')
            s_arr[ord(s_char) - inital] += 1
            t_arr[ord(t_char) - inital] += 1


        return s_arr == t_arr
        