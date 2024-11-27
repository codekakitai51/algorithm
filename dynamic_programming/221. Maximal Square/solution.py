class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
    # true dp bottomo -> up
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [ [0] * (cols + 1) for _ in range(rows + 1) ]

        res = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == '1':
                    right = dp[r][c + 1]
                    down = dp[r + 1][c]
                    diag = dp[r + 1][c + 1]


                    dp[r][c] = 1 + min(right, down, diag)
                    res = max(res, dp[r][c])
        
        return res ** 2

        # memo = {} # map (r, c) -> maxSide

        # def helperDFS(r, c):
        #     if r >= len(matrix) or c >= len(matrix[0]):
        #         return 0
            
        #     if (r, c) in memo:
        #         return memo[(r, c)]
            
        #     down = helperDFS(r + 1, c)
        #     right = helperDFS(r, c + 1)
        #     diag = helperDFS(r + 1, c + 1)

        #     if matrix[r][c] == '1':
        #         memo[(r, c)] = 1 + min(down, right, diag)
        #     else:
        #         memo[(r, c)] = 0
            
        #     return memo[(r, c)]
        
        # helperDFS(0, 0)
        # return max(memo.values()) ** 2
