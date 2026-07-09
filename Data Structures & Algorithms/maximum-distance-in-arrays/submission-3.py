class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curr_min = arrays[0][0]
        curr_max = arrays[0][-1]
        res = 0

        for arr in arrays[1:]:
            min_val = abs(arr[-1] - curr_min)
            most_max = abs(curr_max - arr[0])

            res = max(min_val, most_max, res)

            curr_min = min(arr[0], curr_min)
            curr_max = max(arr[-1], curr_max)

        return res