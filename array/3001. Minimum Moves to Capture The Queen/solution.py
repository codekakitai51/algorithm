class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook_row, rook_col = a, b
        bishop_row, bishop_col = c, d
        queen_row, queen_col = e, f
        
        # Rook in same row as Queen
        if rook_row == queen_row:
            # Bishop blocks Rook or not
            return 2 if bishop_row == rook_row and (rook_col < bishop_col < queen_col or rook_col > bishop_col > queen_col) else 1
        # Rook in same column as Queen
        if rook_col == queen_col:
            # Bishop blocks Rook or not
            return 2 if bishop_col == queen_col and (rook_row < bishop_row < queen_row or rook_row > bishop_row > queen_row) else 1
        # Bishop in same up-diagonal as Queen
        if bishop_row + bishop_col == queen_row + queen_col:
            # Rook blocks Bishop or not
            return 2 if rook_row + rook_col == bishop_row + bishop_col and (bishop_row < rook_row < queen_row or bishop_row > rook_row > queen_row) else 1
        # Bishop in same down-diagonal as Queen
        if bishop_row - bishop_col == queen_row - queen_col:
            # Rook blocks Bishop or not
            return 2 if rook_row - rook_col == bishop_row - bishop_col and (bishop_row < rook_row < queen_row or bishop_row > rook_row > queen_row) else 1
        # If neither the rook nor the bishop can capture the queen in one move, return 2
        return 2