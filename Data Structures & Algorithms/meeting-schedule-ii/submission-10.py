"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        [0, 8]
        [8, 10]

        starttime < endtime
        meeting = 0
        max_meeting = 1
        """
        startTime = sorted([interval.start for interval in intervals])
        endTime = sorted([interval.end for interval in intervals])

        s_ptr= e_ptr = 0
        curr_meeting = 0
        min_meeting = 0

        while s_ptr < len(startTime) and e_ptr < len(endTime):
            if startTime[s_ptr] < endTime[e_ptr]:
                curr_meeting += 1
                s_ptr +=1
            else:
                curr_meeting -=1
                e_ptr += 1

            min_meeting = max(min_meeting, curr_meeting)

        return min_meeting
        