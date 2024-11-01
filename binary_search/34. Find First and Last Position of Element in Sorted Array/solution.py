class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m
            
        if r == len(nums) or nums[r] != target: # if target not found
            return [-1, -1]
        
        # possible to switch to Meguru again here
        firstIdx = r
        while r < len(nums) and nums[r] == target:
            r += 1
        endIdx = r - 1

        return [firstIdx, endIdx]

