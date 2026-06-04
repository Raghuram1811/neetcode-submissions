class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]*len(nums)

        prefix = 1
        for idx in range(len(nums)):
            result[idx] = prefix
            prefix = prefix * nums[idx]
        suffix = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx]*=suffix
            suffix = suffix * nums[idx]
        return result
