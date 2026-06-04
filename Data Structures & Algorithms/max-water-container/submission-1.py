class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right, maxArea = 0, len(heights)-1, 0
        while left<=right:
            area = min(heights[left], heights[right])* (right-left)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
            maxArea = max(maxArea, area)
        return maxArea
