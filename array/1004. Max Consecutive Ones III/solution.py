class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxL = 0
        zeroCount = 0
        s = 0

        for f in range(len(nums)):
            if nums[f] == 0:
                zeroCount += 1
                while zeroCount > k:
                    if nums[s] == 0:
                        zeroCount -= 1
                    s += 1

            maxL = max((f - s) + 1, maxL)
        
        return maxL