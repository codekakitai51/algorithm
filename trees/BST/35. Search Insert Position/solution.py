class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]

            if cur < target:
                l = m + 1
            elif cur > target:
                r = m - 1
            elif cur == target:
                return m
        
        return l