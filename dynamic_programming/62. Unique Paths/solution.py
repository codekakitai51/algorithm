class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        rows = m
        cols = n
        cache = [[0]*n for _ in range(m)]

        # dfs - T: O(2 ^ (m + n)), S: O(m + n) -> Time Limit Exceeded
        # def dfs(r, c):
        #     if r == rows or c == cols: return 0
        #     if r == rows-1 and c == cols-1: return 1

        #     return dfs(r+1, c) + dfs(r, c+1)

        # return dfs(0, 0)

# ------------

        # dfs memoization T, S: O(m * n)
        # def memoization(r, c):
        #     if r == rows or c == cols: return 0
        #     if r == rows-1 and c == cols-1: return 1
        #     if cache[r][c] > 0: return cache[r][c]

        #     cache[r][c] = memoization(r+1, c) + memoization(r, c+1)

        #     return cache[r][c]

        # return memoization(0, 0)

# --------------

        # dp T: O(m * n), S: O(n) ... n is num of cols
        def dp():
            preRow = [0] * cols

            for _ in range(rows-1, -1, -1):
                curRow = [0] * cols
                curRow[-1] = 1
                for revC in range(cols-2, -1, -1):
                    curRow[revC] = curRow[revC+1] + preRow[revC]
                preRow = curRow

            return preRow[0]

        return dp()
