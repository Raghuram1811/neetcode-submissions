class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        search = []
        for rows in matrix:
            if rows[-1] >= target:
                search=rows
                break
    
        return target in search
