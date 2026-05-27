class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        1 2 1
        12

        120
        1

        """
        val = x
        reverse = 0
        while val > 0:
            reverse *= 10
            reverse += (val%10)
            val//=10

        return x == reverse
