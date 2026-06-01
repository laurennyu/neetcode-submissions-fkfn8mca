"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        # Sort by start, ascending order
        times = [(interval.start, interval.end) for interval in intervals]
        times.sort()

        # In reverse order, check that the prev end is not greater than the next start
        next_start = times[-1][0]
        for i in range(len(times)-2, -1, -1):
            if times[i][1] > next_start:
                return False
            
            next_start = times[i][0]

        return True