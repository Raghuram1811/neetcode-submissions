class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)

        
        mini, maxi = min(nums), max(nums)
        seq, max_seq = 0, 0
        for idx in range(mini, maxi+1):
            if idx in nums:
                seq+=1
            else:
                seq = 0
            max_seq = max(max_seq, seq)
        return max_seq