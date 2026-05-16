class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key = lambda x : x[0])

        prev = intervals[0]

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]

            if prev[1] > start:
                prev[1] = min(end, prev[1])
                res += 1
            else:
                prev = intervals[idx]
        return res


