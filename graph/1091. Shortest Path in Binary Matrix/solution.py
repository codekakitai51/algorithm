class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1 # if the start point is blocked, return -1

        distance = 1
        q = deque()
        q.append((0, 0))
        visit = set()
        visit.add((0, 0))
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    print(r, c)
                    return distance

                for dr, dc in directions:
                    if ((r + dr, c + dc) in visit or
                        min(r + dr, c + dc) < 0 or
                        r + dr >= rows or c + dc >= cols or
                        grid[r + dr][c + dc] == 1
                        ): continue
                    
                    visit.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
            
            distance += 1

        return -1
