class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        visited = set()
        maxSizeCount = 0

        def DFS(r, c):
            if (r < 0 or c < 0 or
                r >= ROW or c >= COL or
                grid[r][c] == 0 or
                (r, c) in visited):
                return 0

            visited.add((r, c))

            dire = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            area = 1   # current area

            for x, y in dire:
                area += DFS(r + x, c + y)
            
            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and not (r, c) in visited:
                    maxSizeCount = max(DFS(r, c), maxSizeCount)

        return maxSizeCount