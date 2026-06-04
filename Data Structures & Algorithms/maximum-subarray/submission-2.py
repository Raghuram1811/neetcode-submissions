class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_sum  =  min(nums)
        
        for idx in range(len(nums)):
            total = 0
            for jdx in range(idx, len(nums)):
                total+=nums[jdx]
                max_sum = max(max_sum, total)
        return max_sum