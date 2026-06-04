class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
        
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:

        if left>right:
            return -1

        mid = (left+right)//2
        while left <= right:
            if target < nums[mid]:
                return self.binary_search(nums, left, mid-1, target)
            elif target > nums[mid]:
                return self.binary_search(nums, mid+1, right, target)
            else:
                return mid