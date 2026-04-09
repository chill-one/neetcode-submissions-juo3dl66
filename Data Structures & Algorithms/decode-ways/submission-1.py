class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        first = 1
        second = 0 if s[0] == "0" else 1

        for i in range(2,len(s)+1):
            one = int(s[i - 1])
            two = int(s[i-2:i])
            print(one)
            print(two)
            temp = 0
            if one != 0:
                temp = second

            if two >= 10 and two <= 26:
                temp += first

            first, second = second, temp

        print(dp)
        return second
                