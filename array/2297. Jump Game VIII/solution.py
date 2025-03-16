from typing import List
from collections import deque

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n  # 各インデックスに到達する最小コスト
        dp[0] = 0  # 最初の位置のコストは 0

        # 単調増加スタック（nums[i] <= nums[j] でジャンプするため）
        inc_stack = deque()
        # 単調減少スタック（nums[i] > nums[j] でジャンプするため）
        dec_stack = deque()

        for i in range(n):
            # ① `nums[j]` が `nums[i]` 以下で、`j` から `i` へジャンプできるケース
            while inc_stack and nums[inc_stack[-1]] <= nums[i]:
                j = inc_stack.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])

            # ② `nums[j]` が `nums[i]` より大きく、`j` から `i` へジャンプできるケース
            while dec_stack and nums[dec_stack[-1]] > nums[i]:
                j = dec_stack.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])

            # スタックに現在のインデックス `i` を追加
            inc_stack.append(i)
            dec_stack.append(i)

        return dp[-1]
