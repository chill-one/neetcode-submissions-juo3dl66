class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        nums: integer array
        k : int

        split nums into k non-empty subarrays (we must have atleast 1 number)
            such that the 
                largest sum of any subarray is minimized

        return the minimized largest sum of the split

        mid = minimized largest sum of the split
        max = sum(nums) : 28
        min = min(nums) : 1
        [2, 4, 5, 10, 1, 5] k = 2

        if the mid function < 2:
            move the left up 
        elif the mid function <= k:
            record the value
            keep move the right pointer down
        """

        best = 0
        l, r = max(nums), sum(nums)

        def spot_needed(value):
            res = 1
            load = 0
            for val in nums:
                if load + val > value:
                    res += 1
                    load = 0
                load += val

            return res


        while l <= r:
            m = l + (r - l) // 2
            curr = spot_needed(m)
            print(curr, l , r, m)
            if curr <= k:
                best = m
                r = m - 1
            else:
                l = m + 1


        return best

        