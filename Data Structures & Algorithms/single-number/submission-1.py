class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = nums[0]
        for idx in range(1, len(nums)):
            ans^=nums[idx]
        return ans