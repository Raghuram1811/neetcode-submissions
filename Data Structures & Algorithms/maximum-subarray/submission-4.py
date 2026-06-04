class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        maxValue = nums[0]
        for idx in range(len(nums)):
            current = 0
            for jdx in range(idx, len(nums)):
                current+=nums[jdx]
                maxValue = max(maxValue, current)
        return maxValue