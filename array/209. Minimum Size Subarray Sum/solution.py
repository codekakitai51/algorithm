class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curSum = 0, 0
        length = float("inf")

        for r in range(len(nums)):
            curSum += nums[r]
            
            while curSum >= target:
                length = min(length, r - l + 1)
                curSum -= nums[l]
                l += 1
            
        return 0 if length == float("inf") else length