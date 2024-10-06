class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        dires = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def searchEdgeRegion(r, c):
            if board[r][c] != 'O':
                return
            
            board[r][c] = 'I'

            for x, y in dires:
                if 0 <= r + x < R and 0 <= c + y < C:
                    searchEdgeRegion(r + x, c + y)

        for r in range(R):
            for c in range(C):
                if ((r == 0 or r == R - 1) or (c == 0 or c == C - 1)) and (board[r][c] == 'O'):
                    searchEdgeRegion(r, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'I':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'

