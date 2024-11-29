class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        
        return count


# n^2 too slow
    #     idxSet = set()
    #     for i1 in range(len(nums) - 1):
    #         for i2 in range(i1 + 1, len(nums)):
    #             if (
    #                 i1 not in idxSet and 
    #                 i2 not in idxSet and 
    #                 nums[i1] + nums[i2] == k
    #             ):
    #                 idxSet.add(i1)
    #                 idxSet.add(i2)
        
    #     return len(idxSet) // 2 if idxSet is not None else 0
