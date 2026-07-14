class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def can_ship(cap):
            days_needed = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > cap:
                    days_needed += 1
                    if days_needed > days:
                        return False
                    curr_load = w
                else:
                    curr_load += w
            return True

        best = -1
        while l <= r:
            mid = l + (r - l) // 2
            if can_ship(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1

        return best

