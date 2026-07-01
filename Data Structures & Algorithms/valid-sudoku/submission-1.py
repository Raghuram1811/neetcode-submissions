class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grid = [{} for _ in range(9)]

        for r in range(len(rows)):
            for c in range(len(cols)):

                value = board[r][c]
                if value!='.':
                    grid_dim = r//3 * 3 + c//3

                    if value in rows[r] or value in cols[c] or value in grid[grid_dim]:
                        return False
                    
                    rows[r][value] = True
                    cols[c][value] = True
                    grid[grid_dim][value] = True

        return True