class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(index, curr_list):

            if index == len(nums):
                ans.append(curr_list.copy())
                return
            
            for idx in range(index, len(nums)):

                curr_list[index], curr_list[idx] = curr_list[idx], curr_list[index]
                
                backtrack(index+1, curr_list)

                curr_list[idx], curr_list[index] =  curr_list[index], curr_list[idx]

        backtrack(0, nums)

        return ans