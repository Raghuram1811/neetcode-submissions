class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands=0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=='1':
                    islands+=1
                    self.markZeros(grid, r, c)
        
        return islands

        
    def markZeros(self, grid:List[List[str]], row: int, col: int):

        if row <0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col]=='0':
            return

        grid[row][col]='0'
        
        self.markZeros(grid, row+1, col)
        self.markZeros(grid, row-1, col)
        self.markZeros(grid, row, col+1)
        self.markZeros(grid, row, col-1)
