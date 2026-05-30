class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        . -> any character

        * -> skip, any number of preceding element

        n n n
        n *

        """
        def dfs(i, j):
            #both pointer must go out of bound to be true
            if i >= len(s) and j >= len(p):
                return True

            #if only we get throught p than its false
            if j >= len(p):
                return False

            #current value is a match for both p and s
            match = i < len(s) and (s[i]  == p[j] or p[j] == ".")

            #If the next value is '*' than either skip the astrik (i, j+2) 
            # OR if the current values are a match than we continue with the astricke
            if j + 1 < len(p) and p[j + 1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))

            if match:
                return dfs(i+1, j+1)

            return False

        return dfs(0,0)

            


