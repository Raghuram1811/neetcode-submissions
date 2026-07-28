class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grid = [{} for _ in range(9)]

        for row in range(len(rows)):
            for col in range(len(cols)):

                value = board[row][col]
                if value!='.':
                    grid_dim = row//3 *3 +  col//3
                    if value in rows[row] or value in cols[col] or value in grid[grid_dim]:
                        return False
                    
                    rows[row][value] = True
                    cols[col][value] = True
                    grid[grid_dim][value] = True
        
        return True

