class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key = lambda interval:interval[1])

        kept = 1
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start>=previous_end:
                kept+=1
                previous_end = end
        
        return len(intervals) - kept



