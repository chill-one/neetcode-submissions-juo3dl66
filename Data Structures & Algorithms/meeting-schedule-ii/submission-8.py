"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        

        s = e = 0 
        curr = 0
        minRoom = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s+= 1
                curr += 1
            else:
                e+= 1
                curr -= 1
            minRoom = max(curr, minRoom)

        return minRoom
        