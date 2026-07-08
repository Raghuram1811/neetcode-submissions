class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1

        if nums[0] == target:
            return 0
        
        idx = 0

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                idx = i
                break

        # array is not rotated
        if idx == 0:
            return self.binary_search(nums, target, 0, len(nums)-1)

        # left sorted part: nums[0 : idx]
        # right sorted part: nums[idx : len(nums)]
        if nums[idx] <= target <= nums[-1]:
            return self.binary_search(nums, target, idx, len(nums)-1)
        else:
            return self.binary_search(nums, target, 0, idx-1)


    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1