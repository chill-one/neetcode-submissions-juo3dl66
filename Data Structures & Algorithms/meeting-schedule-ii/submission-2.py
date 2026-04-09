"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        res = count = sPtr = ePtr = 0

        while sPtr < len(start) and ePtr < len(end):
            if start[sPtr] < end[ePtr]:
                sPtr += 1
                count += 1
            elif start[sPtr] >= end[ePtr]:
                ePtr += 1
                count -= 1
            res = max(res, count)

        return res

        