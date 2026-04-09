class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1, max(piles)
        res = high

        while low <= high:
            mid = low + (high - low) // 2

            hours_taken = 0
            for banana in piles:
                hours_taken += math.ceil(banana / mid)
            
            if hours_taken <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1


        return res
