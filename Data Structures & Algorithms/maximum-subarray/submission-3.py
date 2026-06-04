class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, current_sum = nums[0], 0
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum+=num
            maxSub = max(maxSub, current_sum)
        return maxSub