class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        curSum = 0
        maxSum = 0
        left = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            curSum += nums[right]

            if right - left + 1 > k:
                curSum -= nums[left]
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            if right - left + 1 == k and len(count) == k:
                maxSum = max(maxSum, curSum)
            
        return maxSum
