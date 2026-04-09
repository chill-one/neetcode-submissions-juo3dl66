class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        res = 0
        while left <= right:
            print(left, right)
            mid = left + (right - left)//2

            time = 0
            for bananna in piles:
                time += math.ceil(bananna/mid)

            if time <= h:
               res = mid
               right = mid - 1
            else:
                left = mid + 1


        return res 