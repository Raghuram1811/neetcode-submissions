"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals)<2:
            return True
            
        intervals = list(sorted(intervals, key=lambda x:x.end))
        start, end = intervals[0].start, intervals[0].end
        
        for idx in range(1, len(intervals)):
            if end > intervals[idx].start:
                return False
            end = intervals[idx].end
        return True
