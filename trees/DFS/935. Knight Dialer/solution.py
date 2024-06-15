class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        dialTable = [[1] * 3 for _ in range(4)]
        dialTable[3][0], dialTable[3][2] = 0, 0  # '*'と'#'を無効にする
        
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        memo = {}

        def helperDFS(r, c, remaining_moves):
            if r < 0 or r >= 4 or c < 0 or c >= 3 or not dialTable[r][c]:
                return 0
            
            if remaining_moves == 0:
                return 1

            if (r, c, remaining_moves) in memo:
                return memo[(r, c, remaining_moves)]
            
            count = 0
            for x, y in directions:
                count = (count + helperDFS(r + x, c + y, remaining_moves - 1)) % MOD
            
            memo[(r, c, remaining_moves)] = count
            return count

        res = 0
        for r in range(len(dialTable)):
            for c in range(len(dialTable[0])):
                if dialTable[r][c]:
                    res = (res + helperDFS(r, c, n - 1)) % MOD

        return res