class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []
        i = 0
        
        def helper(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return 
 
            # include i
            curSet.append(nums[i])
            helper(i + 1, nums, subsets, curSet)
            curSet.pop()

            # not include i (skip duplicates)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, subsets, curSet)

        helper(i, nums, subsets, curSet)
        return subsets