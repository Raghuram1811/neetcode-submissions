class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right=1, max(piles)
        result = right
        while left<=right:
            middle = (left+right)//2
            totalTime = 0
            for pile in piles:
                totalTime+=math.ceil(float(pile)/middle)

            if totalTime<=h:
                result = middle
                right=middle-1
            else:
                left = middle+1
        return result    
    