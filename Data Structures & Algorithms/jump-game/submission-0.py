class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        fuel = nums[0]
        for num in nums:
            if fuel<0:
                return False
            fuel = max(fuel, num)
            fuel-=1
        return True 