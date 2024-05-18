from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        memo = {}

        def dfs(index, current_sum):
            if current_sum == target:
                return True
            if current_sum > target or index == n:  
                return False
            if (index, current_sum) in memo:  
                return memo[(index, current_sum)]
            
            #  ↓return True immediately if either branch returns True↓
            result = dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)
            memo[(index, current_sum)] = result
            return result
        
        return dfs(0, 0)