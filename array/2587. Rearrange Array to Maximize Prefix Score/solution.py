class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        sumNum, count = 0, 0
        for i in range(len(nums)):
            sumNum += nums[i]
            if sumNum <= 0:
                return count
            
            count += 1
        
        return count