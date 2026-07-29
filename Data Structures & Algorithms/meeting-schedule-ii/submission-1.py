"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key=lambda interval:interval.start)
        ans = []
        ans.append(intervals[0].end)
        heapq.heapify(ans)

        for idx in range(1, len(intervals)):
            if ans[0] <= intervals[idx].start:
                heapq.heappop(ans)
            heapq.heappush(ans, intervals[idx].end)

        return len(ans)
