class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r == 0 and c == 0:  # スタート地点はそのまま
                    continue
                elif r == 0:  # 最初の行（左からのみ移動可能）
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:  # 最初の列（上からのみ移動可能）
                    grid[r][c] += grid[r - 1][c]
                else:  # 上と左から移動可能
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[r][c]