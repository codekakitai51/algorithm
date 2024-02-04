class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == '0' or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for v, h in directions:
                dfs(r+v, c+h)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    count += 1
                    dfs(r, c)
        
        return count
    # Time complexity: O(4**(r*c)) Space complexity: O(r*c)
