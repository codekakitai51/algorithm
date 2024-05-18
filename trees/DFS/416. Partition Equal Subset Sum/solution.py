from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # 総和が奇数の場合、等しい部分集合に分けることはできません。
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        memo = {}

        def dfs(index, current_sum):
            if current_sum == target:  # 目標値に達した場合はTrue
                return True
            if current_sum > target or index == n:  # 範囲外または合計が目標を超えた場合はFalse
                return False
            if (index, current_sum) in memo:  # メモ化された結果を利用
                return memo[(index, current_sum)]
            
            # 現在の要素を含める場合と含めない場合の結果を計算
            result = dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)
            memo[(index, current_sum)] = result  # 結果をメモ化
            return result
        
        return dfs(0, 0)