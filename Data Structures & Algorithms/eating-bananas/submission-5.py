class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        result = left

        while left<=right:
            middle = (left+right)//2
            total_time = 0
            for pile in piles:
                total_time+=math.ceil(pile/middle)

            if total_time > h:
                left = middle+1
            else:
                result = middle
                right = middle-1
                    
        return result
        
