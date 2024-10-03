class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dire = [(-1, 0),  # 上
                (1, 0),   # 下
                (0, -1),  # 左
                (0, 1),   # 右
                (-1, -1), # 左上
                (-1, 1),  # 右上
                (1, -1),  # 左下
                (1, 1)]   # 右下

        R, C = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                liveNei = 0
                for x, y in dire:
                    if 0 <= r + x < R and 0 <= c + y < C:
                        # 中間状態も含めて生きているセルをカウントするためにabsを使用
                        if abs(board[r + x][c + y]) == 1:
                            liveNei += 1
                
                if board[r][c] == 1:  # 生きているセル
                    if liveNei < 2 or liveNei > 3:
                        board[r][c] = -1  # 生きていたセルが死ぬ
                else:  # 死んでいるセル
                    if liveNei == 3:
                        board[r][c] = 2  # 死んでいたセルが生きる

        # 状態をリセットして、新しい世代に更新
        for r in range(R):
            for c in range(C):
                if board[r][c] == -1:
                    board[r][c] = 0  # 生きていたが死んだセル
                elif board[r][c] == 2:
                    board[r][c] = 1  # 死んでいたが生き返ったセル
