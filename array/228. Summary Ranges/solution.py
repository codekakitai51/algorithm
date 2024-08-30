from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        l = 0

        for r in range(1, len(nums) + 1):
            if r == len(nums) or nums[r] != nums[r - 1] + 1:
                if l == r - 1:
                    res.append("{}".format(nums[l]))
                else:
                    res.append("{}->{}".format(nums[l], nums[r - 1]))
                l = r
        
        return res
