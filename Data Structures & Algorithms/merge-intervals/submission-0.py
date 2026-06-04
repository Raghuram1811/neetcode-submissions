class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda interval: interval[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(end, lastEnd)
            
            else:
                output.append([start, end])
        return output
