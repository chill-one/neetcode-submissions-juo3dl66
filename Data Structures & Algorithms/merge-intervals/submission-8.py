class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort by starttime
        intervals.sort(key= lambda x: x[0])


        res = [intervals[0]]

        #We start the itteration after the first interval
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]

            #If the current start time is less than the previous end time its a overlape
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append(intervals[idx])


        return res



