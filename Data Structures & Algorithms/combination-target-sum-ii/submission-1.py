class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        candidates.sort()

        def dfs(idx, cur, total):

            if total == target:
                res.add(tuple(cur.copy()))
                return
            if idx==len(candidates) or total > target:
                return 
            
            cur.append(candidates[idx])
            dfs(idx+1, cur, total+candidates[idx])

            cur.pop()

            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            dfs(idx+1, cur, total)
        
        dfs(0, [], 0)
        return [list(elem) for elem in res]