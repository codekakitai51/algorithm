class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        lenWord = len(word)
        
        # ボードのサイズが単語の長さより小さい場合は、即座にFalseを返す
        if R * C < lenWord:
            return False
        
        # 上下左右の方向
        dires = [
            (0, 1),   # 右
            (0, -1),  # 左
            (-1, 0),  # 上
            (1, 0)    # 下
        ]

        # バックトラッキング関数
        def backtracking(r, c, wordIdx):
            # 全ての文字を見つけたらTrue
            if wordIdx == lenWord:
                return True
            
            # 境界チェックと単語が一致するか確認
            if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[wordIdx]:
                return False
            
            # 一時的にセルを使用済みとしてマーク（再訪問を防ぐ）
            temp = board[r][c]
            board[r][c] = '#'
            
            # 4方向に探索
            for x, y in dires:
                if backtracking(r + x, c + y, wordIdx + 1):
                    return True
            
            # 探索が終わったら元に戻す
            board[r][c] = temp
            
            return False

        # ボード上の各セルを開始点として探索を開始
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0):
                        return True
        
        return False
