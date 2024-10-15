class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0
        
        for num in nums:
            # 通常のKadane'sアルゴリズム（最大部分配列を探す）
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            
            # 最小部分配列を探すためのKadane'sアルゴリズム
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            
            totalSum += num
        
        # すべての数が負の場合（全体が最小部分配列と同じ場合）
        if totalSum == minSum:
            return maxSum
        
        # 通常の最大部分配列と巻き戻りを考慮した部分配列の最大値の比較
        return max(maxSum, totalSum - minSum)
