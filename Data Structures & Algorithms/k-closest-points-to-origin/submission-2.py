class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            result = heapq.heappop(maxHeap)
            res.append([result[1], result[2]])
        return res