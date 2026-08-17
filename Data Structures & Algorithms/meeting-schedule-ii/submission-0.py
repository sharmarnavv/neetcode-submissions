"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        days = 1
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                days += 1
        return days