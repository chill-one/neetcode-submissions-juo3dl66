class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        for num in range(x + 1):
            if num * num > x:
                return num - 1

        return 0