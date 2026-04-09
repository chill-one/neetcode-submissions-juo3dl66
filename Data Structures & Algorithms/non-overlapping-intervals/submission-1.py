class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,100],[1,11],[2,12],[11,22]]

        """
        intervals.sort(key=lambda x : x[0])
        res = 0
        prevEnd = intervals[0][1]

        for idx in range(1, len(intervals)):
            arr = intervals[idx]

            if prevEnd <= arr[0]:
                prevEnd = arr[1]
            else:
                res += 1
                prevEnd = min(arr[1], prevEnd)

        return res

        
