class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda interval:interval[1])

        kept = 1

        latest = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= latest:
                kept+=1
                latest = end
        return len(intervals) - kept
