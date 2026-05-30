class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            count = 0
            val = i
            while val > 0:
                if val & 1:
                    count += 1
                val >>= 1

            res.append(count)

        return res