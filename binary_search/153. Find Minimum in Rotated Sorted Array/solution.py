class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] <= nums[-1]:
                r = m
            else:
                l = m
        
        return nums[r]

# めぐる式のポイントはl, rどちらかは常に条件を満たす、片方は常に条件を満たさないにすると解きやすい