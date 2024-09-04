class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        c = 0

        while r < len(nums) and c + r < len(nums):
            if nums[l] == nums[r]:
                if (r - l) + 1 > 2:
                    # shift
                    for i in range(r + 1, len(nums)):
                        nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    c += 1
                else:
                    r += 1
            else:
                l = r
                r += 1

        return r

# T: O(n) better but, hard to come up with 
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     i = 1
    #     j = 1
    #     count = 1

    #     while i < len(nums):
    #         if nums[i] == nums[i - 1]:
    #             count += 1
    #             if count > 2:
    #                 i += 1
    #                 continue
    #         else:
    #             count = 1
    #         nums[j] = nums[i]
    #         j += 1
    #         i += 1

    #     del nums[j:]
    #     return len(nums)