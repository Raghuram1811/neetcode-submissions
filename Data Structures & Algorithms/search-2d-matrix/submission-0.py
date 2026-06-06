class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for rows in matrix:
            for num in rows:
                if num == target:
                    return True
        return False