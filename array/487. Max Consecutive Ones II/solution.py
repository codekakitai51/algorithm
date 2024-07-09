class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        maxCount = 0
        numZeros = 0

        count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1

            while numZeros >= 2:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            
            maxCount = max(maxCount, r - l + 1)
        
        return maxCount
