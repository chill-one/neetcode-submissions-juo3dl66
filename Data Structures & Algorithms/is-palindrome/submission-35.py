class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        new_str = s.lower()
        while left <= right:

            while left < right and not new_str[left].isalnum():
                left += 1

            while right > left and not new_str[right].isalnum():
                right -= 1

            if new_str[left] != new_str[right]:
                return False

            left +=1
            right -= 1

        return True

