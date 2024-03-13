from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        dire = [[0, 1], [-1, 0], [0, -1], [1, 0]]       
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dire:
                    if (x + dx < 0 or y + dy < 0 or
                        x + dx == ROWS or y + dy == COLS or
                        grid[x + dx][y + dy] != 1):
                        continue

                    grid[x + dx][y + dy] = 2
                    q.append([x + dx, y + dy])
                    fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1
    

