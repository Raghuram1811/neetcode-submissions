class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = deque()

        def bfs(r, c):
            visited.add((r,c))
            queue.append((r,c))
            area = 1

            while queue:
                row, col = queue.popleft()

                for nx, ny in directions:
                    x, y = row+nx, col+ny
                    if 0<=x<rows and 0<=y<cols and grid[x][y]==1 and (x, y) not in visited:
                        visited.add((x, y))
                        area+=1
                        queue.append((x, y))
            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea