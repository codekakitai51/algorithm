class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = curSum = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            curSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, curSum)
        
        return maxSum / k