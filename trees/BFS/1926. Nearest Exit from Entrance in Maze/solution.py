class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])  # キューには現在の位置とステップ数を保存
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            curR, curC, steps = queue.popleft()

            for dr, dc in directions:
                nextR, nextC = curR + dr, curC + dc

                if 0 <= nextR < m and 0 <= nextC < n and (nextR, nextC) not in visited and maze[nextR][nextC] == '.':
                    # 出口に到達した場合
                    if (nextR == 0 or nextR == m - 1 or nextC == 0 or nextC == n - 1) and [nextR, nextC] != entrance:
                        return steps + 1

                    queue.append((nextR, nextC, steps + 1))
                    visited.add((nextR, nextC))

        return -1

# Time complexity: O(m * n)
# Space complexity: O(m * n)

    
# Time complexity: O(m * n)
# Space complexity: O(m * n)

# if you need to have element that should be unique, use set() instead of list() to store them