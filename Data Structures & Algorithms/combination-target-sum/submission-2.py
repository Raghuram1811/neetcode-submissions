class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(index, curr_list, total):

            if index >= len(nums) or total > target:
                return 
            
            if total == target:
                res.append(curr_list.copy())
                return
            
            curr_list.append(nums[index])
            backtrack(index, curr_list, total+nums[index])

            curr_list.pop()
            backtrack(index+1, curr_list, total)
        
        backtrack(0, [], 0)
        return res

