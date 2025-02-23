class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        L = len(nums)
        minN, minI = float("inf"), -1
        maxN, maxI = float("-inf"), -1

        for i in range(L):
            if minN > nums[i]:
                minN = nums[i]
                minI = i
            
            if maxN <= nums[i]:
                maxN = nums[i]
                maxI = i
        
        if minI > maxI:
            maxI += 1 # minN swaps help maxN swaps once
        return minI + ((L - maxI) - 1)
        