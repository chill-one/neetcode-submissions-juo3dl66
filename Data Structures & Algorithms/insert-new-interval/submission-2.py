class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [[1,2],[3,5],[9,10]] [6,7]
        """

        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]

            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] <= end:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[-1])
            else:
                res.append([start, end])
        res.append(newInterval)
        return res
