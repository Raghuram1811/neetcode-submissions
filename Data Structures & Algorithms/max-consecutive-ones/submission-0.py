class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, max_ones = 0, 0
        for idx, num in enumerate(nums):
            if num==1:
                counter+=1
                max_ones = max(max_ones, counter)
            else:
                counter=0
        return max_ones
            