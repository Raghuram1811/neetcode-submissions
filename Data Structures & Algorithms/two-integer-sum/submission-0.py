class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = dict()
        for idx, num in enumerate(nums):
            if num in check:
                return [check[num], idx]
            check[target-num] = idx
        return [-1, -1]