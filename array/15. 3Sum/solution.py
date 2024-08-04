class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i):
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    # 重複をスキップ
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                twoSum(i)
                 
        return res