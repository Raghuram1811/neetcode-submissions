class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(idx, curr_list):

            if idx >= len(nums):
                ans.append(curr_list.copy())
                return
            
            curr_list.append(nums[idx])

            backtrack(idx+1, curr_list)
        
            curr_list.pop()

            backtrack(idx+1, curr_list)
        
        backtrack(0, [])
        
        return ans
            
            

