class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def isPal(l, r):
            while l < r :
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1

            return True


        while left < right:
            if s[left] == s[right]:
                left +=1
                right -= 1
                continue

            if isPal(left+1, right) or isPal(left, right-1):
                return True
            else:
                return False
            


        return True