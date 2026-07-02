class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0 

        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        

        def bfs(r, c):

            queue = deque()
            queue.append((r, c))
            visited.add((r,c))
            perimeter = 0

            while queue:

                row, col = queue.popleft()
                for nr, ny in directions:
                    x, y = row+nr, col+ny
                    if x < 0 or x >= rows or y < 0 or y>= cols or grid[x][y]==0:
                        perimeter+=1
                    elif (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
            return perimeter



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return bfs(r,c)
        return 0