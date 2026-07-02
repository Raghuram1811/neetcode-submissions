class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]=="1":
                    ans+=1
                    self.markZeros(grid, row, col)
        return ans
        
    def markZeros(self, grid:List[List[str]], row: int, col:int):

        if row<0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col]=='0':
            return 
        
        grid[row][col] ="0"
        self.markZeros(grid, row+1, col)
        self.markZeros(grid, row-1, col)
        self.markZeros(grid, row, col+1)
        self.markZeros(grid, row, col-1)
