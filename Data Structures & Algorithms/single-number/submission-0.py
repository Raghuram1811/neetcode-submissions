class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        first = nums[0]
        for idx in range(1, len(nums)):
            ans = first^nums[idx]
            first = ans
        return first