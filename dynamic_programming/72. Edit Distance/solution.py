class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
# true dp
        dp = [ [float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1) ]

    # preset for edge values
        val = 0
        for r in range(len(word1), -1, -1):
            dp[r][len(word2)] = val
            val += 1
        val = 0
        for c in range(len(word2), -1, -1):
            dp[len(word1)][c] = val
            val += 1
        
    # now we can do dp operation
        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(
                        dp[r + 1][c],
                        dp[r][c + 1],
                        dp[r + 1][c + 1]
                    )
        
        return dp[0][0]
        
        
#  memolization m * n

        # memo = {}

        # def dfs(i1, i2):
        #     # 終了条件：片方が文字列の末尾に到達
        #     if i1 == len(word1):
        #         return len(word2) - i2  # 残りの文字数を挿入
        #     if i2 == len(word2):
        #         return len(word1) - i1  # 残りの文字数を削除

        #     # メモ化済みならその結果を返す
        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]

        #     # 再帰処理
        #     if word1[i1] == word2[i2]:
        #         # 一致する場合、次の文字へ進む
        #         result = dfs(i1 + 1, i2 + 1)
        #     else:
        #         # 一致しない場合、挿入・削除・置換の最小値を取る
        #         insert = dfs(i1, i2 + 1) + 1    # 挿入
        #         delete = dfs(i1 + 1, i2) + 1   # 削除
        #         replace = dfs(i1 + 1, i2 + 1) + 1  # 置換
        #         result = min(insert, delete, replace)

        #     # メモ化
        #     memo[(i1, i2)] = result
        #     return result

        # return dfs(0, 0)
