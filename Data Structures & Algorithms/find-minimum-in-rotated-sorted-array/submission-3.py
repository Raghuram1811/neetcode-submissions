class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1

        minima = nums[0]

        while left<=right:

            if nums[left] < nums[right]:
                return min(minima, nums[left])
            
            middle = (left+right)//2
            minima = min(nums[middle], minima)

            if nums[middle] >= nums[left]:
                left = middle+1
            else:
                right = middle -1
        return minima
