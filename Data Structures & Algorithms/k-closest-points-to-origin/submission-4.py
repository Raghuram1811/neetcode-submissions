class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        closest = []
        heapq.heapify(closest)

        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(closest, [dist, x, y])

            if len(closest) > k:
                heapq.heappop(closest)
        
        for point in closest:
            res.append([point[1], point[2]])
        return res