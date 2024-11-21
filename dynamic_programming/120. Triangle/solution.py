from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for c in range(r + 1):
                smallestAbove = math.inf

                if c > 0:
                    smallestAbove = triangle[r - 1][c - 1]
                if c < r:
                    smallestAbove = min(smallestAbove, triangle[r - 1][c])

                triangle[r][c] += smallestAbove
            
        return min(triangle[-1])

        # def DFS(r, i):
        #     # ベースケース: 最下層に到達した場合
        #     if r == len(triangle):
        #         return 0

        #     # メモ化の確認
        #     if (r, i) in memo:
        #         return memo[(r, i)]

        #     # 再帰的に下層のパス和を計算
        #     left = DFS(r + 1, i)
        #     right = DFS(r + 1, i + 1)

        #     # 現在位置の最小パス和をメモ化
        #     memo[(r, i)] = triangle[r][i] + min(left, right)
        #     return memo[(r, i)]

        # memo = {}
        # return DFS(0, 0)
