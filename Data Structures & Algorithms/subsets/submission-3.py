class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(index, curr_list):

            if index>=len(nums):
                res.append(curr_list.copy())
                return
            
            curr_list.append(nums[index])

            backtrack(index+1, curr_list)

            curr_list.pop()

            backtrack(index+1, curr_list)
        
        backtrack(0, [])
        return res

            